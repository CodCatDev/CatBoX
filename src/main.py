from pack import makeCbox
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("ERROR: No argv payload")
    print("Use:")
    print("     python3 src/main.py {fileToPack} -o {outputFile}")

file = None
meta = None
output = "myArchive.cbox"
try:
    file = args[0]
    meta = args[1]
    output = args[2]
except:
    pass

if meta and not output:
    print("ERROR: No output file payload")
    print("Use:")
    print("     python3 src/main.py {fileToPack} -o {outputFile}")

makeCbox(output, file)
print("Done!")