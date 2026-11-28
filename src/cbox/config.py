
class BuildInfo:
    Version = "0.2.2"
    Build = "1"
    Branch = "dev"
    FormatSpec = "v1"

class Magic:
    Text = "CBOX"
    Bytes = Text.encode("ascii")
    Hex = Bytes.hex(" ").upper() 