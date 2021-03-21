"""
Take the file list of godot class .rst names and convert
them into a series of links to the godot api on the web

The source file is to be called godot_api.txt and the output is a .json file
"""

import json
import logging
import re
from argparse import ArgumentParser, Namespace
from pathlib import PurePath
import sys
from typing import List
from fastcore.basics import true
from ghapi.actions import github_token

from ghapi.all import GhApi

LOGGER = logging.getLogger("Make Godot API references")
LOG_LEVELS = [logging.INFO, logging.DEBUG]
LOG_LEVELS = [None] + sorted(LOG_LEVELS, reverse=True)

def parse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        description="Given a godot-docs branch it scans the class folder "
        "and creates a JSON file linking the Godot class name with the API reference",
    )

    parser.add_argument(
         "--token", 
        type=str,
        default = "",
        help='optional github access token (default "" may only gives 60 reads/hour)'
    )

    parser.add_argument(
        "--branch",
        type=str,
        default="stable",
        help="optional branch for the class files (default: stable)"
    )
    
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Set the verbosity level. For example -vv sets verbosity to level 2. Default: 0."
    )

    parser.add_argument(
        "--check-branches",
        action="store_true",
        help="print out a list of the Godot document branches then exit without making the links"
    )
    
    # parser.add_argument("-V", "--version", action="store_true", help="Print the version number and exit,")
    
    namespace: Namespace = parser.parse_args()
    # namespace.verbose = 9999 if namespace.dry_run else namespace.verbose
    return namespace

def get_godot_classes(git_token = "", branch = "stable"):
    api = GhApi(token=git_token)
    LOGGER.info(
        " Connected to Github with {} requests remaining".format(api.limit_rem) 
    )
    files: List = api.repos.get_content("godotengine", "godot-docs", "classes", branch)
    return files

def get_godot_branches(git_token: str = ""):
    api = GhApi(owner="godotengine", repo="godot-docs", token=git_token)
    branches = api.list_branches()
    return branches

def main():
    args: Namespace = parse()

    git_token =  args.token
    branch =  args.branch

    if args.check_branches:
        branches = get_godot_branches(git_token)
        for branch in branches:
            print(PurePath(branch.ref).name)
        sys,exit()

    logging.basicConfig(level = LOG_LEVELS[min(args.verbose, len(LOG_LEVELS) - 1)])

    api_files: List = get_godot_classes(git_token, branch)
    
    api_calls = {}
    for i in api_files:
        file_stem = PurePath(i.name).stem
        LOGGER.debug(
            " processing file: {}".format(i.name)
        )
        class_name = re.search("class_([a-z0-9@]+)", file_stem)
        if class_name != None:
            LOGGER.debug(
                " extracted class name as: {}".format(class_name.group(1))
            )
            class_str: str = class_name.group(1)
            LOGGER.debug(
                " created link {} -> https://docs.godotengine.org/en/{}/classes/class_{}.html".format(class_str, branch, class_str)
            )
            api_calls[class_str] = "https://docs.godotengine.org/en/{}/classes/class_{}.html".format(branch, class_str)
        else:
            LOGGER.debug(
                 " ignoring: {}".format(file_stem)
            )
            LOGGER.info(
                " ignoring: {}".format(i.name)
            )

    with open("godot_api_calls.json", "w") as json_file:
        LOGGER.info(
            " Saving data to {}".format(json_file.name)
        )
        json.dump(api_calls, json_file, indent=4)

    print("Finished!")

if __name__ == "__main__":
    main()
