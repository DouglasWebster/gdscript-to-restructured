"""
Merges JSON dumped by Godot's script language server and converts
it to a rest document formated in the look and feel of the Godot
API documentaion
"""

import json
import logging
import os
import sys
from argparse import Namespace
from itertools import repeat
from typing import List

from .src import command_line
from .src.config import LOG_LEVELS, LOGGER
from .src.gdscript_objects import GDScriptClasses, ProjectInfo
from .src.make_restructured import RestructuredDocument
from .src.convert_to_restructured import convert_to_restructured


def main():
    args: Namespace = command_line.parse()

    if args.version:
        print("GDScript REST Doc Maker version 0.1.1")
        sys.exit()
    
    logging.basicConfig(level = LOG_LEVELS[min(args.verbose, len(LOG_LEVELS) - 1)])
    json_files: List[str] = [f for f in args.files if f.lower().endswith(".json")]
    LOGGER.info("Processing JSON files: {}".format(json_files))
    for f in json_files:
        with open(f,"r") as json_file:
            data: list = json.loads(json_file.read())
            
            if data["version"] == None:
                LOGGER.info(
                    "Project has no version number - setting it to {}".format(args.doc_version)
                )
                data["version"] = args.doc_version

            project_info: ProjectInfo = ProjectInfo.from_dict(data)
            if project_info.version == None:
                project_info.version =="0.0.0"
            classes: GDScriptClasses = GDScriptClasses.from_dict_list(data["classes"])
            classes_count: int = len(classes)

            LOGGER.info(
                "Project {}, version {}".format(project_info.name, project_info.version)
            )

            LOGGER.info(
                "Processing {} classes in {}".format(classes_count, os.path.basename(f))
            )

            documents: List[RestructuredDocument] = convert_to_restructured(
                classes, args, project_info
            )

            if args.dry_run:
                LOGGER.debug("Generated {} reStructured documents.".format(len(documents)))
                list(map(lambda doc: LOGGER.debug(doc), documents))
            else:
                if not os.path.exists(args.path):
                    LOGGER.info("Creating directory " + args.path)
                    os.mkdir(args.path)
                
                LOGGER.info(
                    "Saving {} reStructured files to {}".format(len(documents), args.path)
                )
                list(map(save, documents, repeat(args.path)))


def save(
    document: RestructuredDocument,
    dirpath: str
):
    path: str = os.path.join(dirpath, document.get_filename())
    with open(path, "w") as file_out:
        LOGGER.debug("Saving reStructured file " + path)
        file_out.write(document.as_string())

            
if __name__== "__main__":
    main()
