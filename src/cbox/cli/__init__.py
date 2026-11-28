import argparse
from .tools import Tools

def runCLI():

    parser=argparse.ArgumentParser(
        prog="cbox",
        description="Pack files into .CBoX archive files",
        suggest_on_error=True,
        add_help=True,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("file", help="file to pack")
    parser.add_argument("-o", "--output", default="myArchive.cbox",
                        help="output archive (default: myArchive.cbox)")
    parser.add_argument('-v', '--version', action='version', version=Tools.version(), help="show program's version info and exit")
    parser.add_argument('-i', '--info', action='version', version=Tools.info(), help="show program's dev information and exit")

    args = parser.parse_args()
    print(args)