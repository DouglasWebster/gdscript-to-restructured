"""
Take the file list of godot class .rst names and convert
them into a series of links to the godot api on the web

The source file is to be called godot_api.txt and the output is a .json file
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List


def main():
    base_dir = Path("/home/douglas/Projects/godot-docs/classes")
    api_files: List = base_dir.glob("./*.rst")
    
    api_calls = {}
    for i in api_files:
        print(i.stem)
        class_name = re.search("class_([a-z0-9@]+)", i.stem)
        if class_name != None:
            class_str: str = class_name.group(1)
            print("\"{}\": \"https://docs.godotengine.org/en/stable/classes/class_{}.html\"".format(class_str, class_str))
            api_calls[class_str] = "https://docs.godotengine.org/en/stable/classes/class_" + class_str + ".html"

    with open("godot_api_calls.json", "w") as json_file:
        json.dump(api_calls, json_file)

    print("Finished!")

main()
