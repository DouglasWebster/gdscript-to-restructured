# import datetime
import sys
from argparse import ArgumentParser, Namespace


def parse(args=sys.argv) -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog = "gdscript2rest",
        description="Converts JSON data dumped by Godot's "
        "GDScript language server to create .rst files for "
        "use with Sphinx.",
    )

    args.pop(0)  # we dont want the file list polluted with the program name.

    parser.add_argument("files", type=str, nargs="+", help="A list of paths to JSON files.")
    parser.add_argument("-p", "--path", type=str, default="export", help="Path to the output directory.")
    parser.add_argument("-i", "--make-index", action="store_true", default=False, help="If this flag is present, create and index.rst page with a table of contents.")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Set the verbosity level. For example -vv sets verbosity to level 2. Default: 0.")
    parser.add_argument("--dry-run", action="store_true", help="Run the script at max verbosity without creating files.  For debugging purposes.")
    parser.add_argument("-V", "--version", action="store_true", help="Print the version number and exit,")
    parser.add_argument("--doc-version", type=str, default="0.0.0", help="Set the document version number if there is no version set in the JSON file. Defaults to 0.0.0")

    namespace: Namespace = parser.parse_args(args)
    namespace.verbose = 9999 if namespace.dry_run else namespace.verbose
    return namespace
