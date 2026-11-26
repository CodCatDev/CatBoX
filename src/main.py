from pack import makeCbox
import argparse
import const

def main():
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
    parser.add_argument('-v', '--version', action='version', version=const.VersionInfo)
    args = parser.parse_args()
    print(args)

if __name__ == "__main__": 
    main()