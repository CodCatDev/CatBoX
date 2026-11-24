import struct

# \x01 = archive start
# \x02 = file metadata
# \x03 = data separator
# \x04 = start file data
# \x00 = end of archive

FileMagic = b"CBX\x02"
FileStart = b"\x03CBX\x04"
ArchiveEnd = b"\x03CBX\x00"

def makeCbox(name: str, file: str) -> bool:
    print("[LOG] Packing...")
    if not name.endswith(".cbox"):
        name = f"{name}.cbox"
        print("[WARN] Not founded suffix .cbox in OutputFile, addeding it automaticly.")
    with open(name, "wb") as f:
        print(f"[LOG] Creating {name}")
        f.seek(0)
        print("[LOG] Writing metadata")
        f.write(struct.pack("4s", b"CBOX\x01")) # magic
        f.write(struct.pack("<H", 1)) # version
        f.write(struct.pack("<I", 1)) # files count

        print("[LOG] Writing files")
        f.write(FileMagic) # marker: file data start
        f.write(file.encode('utf-8'))
        f.write(FileStart)
        with open(f"{file}", "rb") as mf:
            mf.seek(0)
            f.write(mf.read()) # write file

        f.write(ArchiveEnd)
        print("[LOG] Saving archive..")