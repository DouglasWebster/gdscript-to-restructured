"""
Uses the parsed GDScriptClasses dictionary parsed from the JSON
data to output the reStructuredText documents
"""

import json
import re
from argparse import Namespace
from typing import List

from .config import LOGGER
from .gdscript_objects import (Element, GDScriptClass, GDScriptClasses,
                               ProjectInfo)
from .make_restructured import (RestructuredDocument, RestructuredSection,
                                make_bold, make_code_block, make_comment,
                                make_heading, make_link, make_table_header,
                                make_table_row, surround_with_html,
                                wrap_in_newlines, make_prop_table,
                                make_element, make_func_table)


def convert_to_restructured(
    classes: GDScriptClasses, arguments: Namespace, info: ProjectInfo
) -> List[RestructuredDocument]:
    """
    Takes a list of dictionaries, each one representing a GDScript class
    and  converts it to reStructuredText.  It returns a list of
    reStructuredText documents.
    """
    restructured: List[RestructuredDocument] = []
    if arguments.make_index:
        restructured.append(_write_index_page(classes, info))
    for entry in classes:
        restructured.append(_as_restructured(classes, entry, arguments))
    return restructured

def _as_restructured(
    classes: GDScriptClasses, gdscript: GDScriptClass, arguments: Namespace
) -> RestructuredDocument:
    """
    Converts the data from a GDScript class into reStructuredText.
    """

    content: List[str] = []

    name: str = gdscript.name

    doc_ref: str = "class_" + name
    
    if "abstract" in gdscript.metadata.tags:
        name += " " + surround_with_html("(abstract)", "small")

    content += [
        make_comment(
            "Auto-generated from JSON by GDScript restructured maker.\n"
            "Do not edit this document directly as all changes will be\n"
            "to be overwritten on the next auto-generation." 
        )
        + "\n\n"
        + ".. _{}:".format(doc_ref) 
    ]

    content += [*make_heading(name, 1)]
    if gdscript.extends:
        extends_list: List[str] = gdscript.get_extends_tree(classes)
        extends_links = [make_link(entry) for entry in extends_list]
        content += [make_bold("Extends:") + " " + " < ".join(extends_links)]
        description = _replace_references(classes, gdscript, gdscript.description)
        content += [*RestructuredSection("Description", 2, [description]).as_text()]

    content += _write_class(classes, gdscript, 2)
    # if gdscript.signals:
    #     content += RestructuredSection(
    #         "Signals", 2, _write_signals(classes, gdscript)
    #     ).as_text()

    if gdscript.sub_classes:
        content += make_heading("Sub-classes", 2)
    for cls in gdscript.sub_classes:
        content += _write_class(classes, cls, 3, True)

    return RestructuredDocument(gdscript.name, doc_ref, content)

    
    
def _write_class(
    classes: GDScriptClasses,
    gdscript: GDScriptClass,
    heading_level: int,
    is_inner_class: bool = False,
) -> List[str]:
    restructured: List[str] = []
    if is_inner_class:
        restructured += make_heading(gdscript.name, heading_level)
    for attribute, title, table in [
        ("members", "Properties", True),
        ("functions", "Methods", True),
        ("signals", "Signals", False),
        ("enums", "Enumerations", False),
        ("constants", "Constants", False),
        ("members", "Propertry Descriptions", False),
        ("functions", "Method Descriptions", False),
    ]:
        if not getattr(gdscript, attribute):
            continue
        restructured += RestructuredSection(
            title,
            heading_level + 1 if is_inner_class else heading_level,
            _write(attribute, classes, gdscript, table),
        ).as_text()
    return restructured




def _writ_summary(gdscript: GDScriptClass, key: str) -> List[str]:
    element_list = getattr(gdscript, key)
    if not element_list:
        return []
    restructured: List[str] = make_table_header(["Type", "Name"])
    return restructured + [make_table_row(item.summerize()) for item in element_list]


def _write(
    attribute: str,
    classes: GDScriptClasses,
    gdscript:GDScriptClass,
    table: bool,
    heading_level: int = 3
) -> List[str]:
    assert hasattr(gdscript, attribute)
    
    restructured: List[str] = []
    element = getattr(gdscript, attribute)
    if table:
        if attribute == "members":
            restructured.extend(make_prop_table(element, gdscript.name))
        else:
            restructured.extend(make_func_table(element, gdscript.name))
    else:
        restructured.extend(make_element(attribute, element, gdscript.name))
        # for element in getattr(gdscript, attribute):
        #     # restructured.extend(make_heading(element.get_heading_as_string(), heading_level))
        #     restructured.extend([make_code_block(element.signature), ""])
        #     restructured.extend(element.get_unique_attributes_as_restructured())
        #     restructured.append("")
        #     description: str = _replace_references(classes, gdscript, element.description)
        #     restructured.append(description)

    return restructured

def _write_signals(classes:GDScriptClasses, gdscript: GDScriptClass) -> List[str]:
    return wrap_in_newlines(
        [
            "- **{}**\n\n{}".format(
                s.signature.split(' ', 1)[1],
                _replace_references(classes, gdscript, s.description)
            )
            for s in gdscript.signals
        ]
    )


def _write_index_page(classes: GDScriptClasses, info: ProjectInfo) -> RestructuredDocument:
    title: str = "{}".format(info.name)
    version: str = "Version: {}".format(info.version)
    content: List[str] =[
        *RestructuredSection(title, 1, [version] + [""] + [info.description]).as_text(),
        *RestructuredSection("Contents", 2, _write_table_of_contents(classes)).as_text()
    ]
    return RestructuredDocument("index", "", content)

def _write_table_of_contents(classes: GDScriptClasses) -> List[str]:
    toc: List[str] = [
        "..  toctree::",
        "    :maxdepth: 1",
        "    :caption: API",
        "    :glob:",
        "\n    *"
    ]

    return toc


def _replace_references(
    classes: GDScriptClasses, gdscript: GDScriptClass, description: str
) -> str:
    """
    Finds and replaces references to other classes or methods in the description.
    """
    ERROR_MESSAGE = {
        "class": "Class {} not found in the class index.",
        "member": "Symbol {} not found in {}.  The name might be incorrect.",
    }
    ERROR_TAIL = "The name might be incorrect."

    references: re.Match = re.findall(r"\[,+\]", description)
    for reference in references:
        # Matches [ClassName], [symbol] and [ClassName.symbol]
        match: re.Match = re.match(
            r"\[([A-Z][a-zA-Z0-9]*)?\.?([a-z0-9_]+)?\]", reference
        )
        if not match:
            continue

        class_name, member = match[1], match[2]

        if class_name and class_name not in classes.class_index:
            LOGGER.warning(ERROR_MESSAGE["class"].format(class_name) + ERROR_TAIL)
            continue

        if member and class_name:
            if member not in classes.class_index[class_name]:
                LOGGER.warning(
                    ERROR_MESSAGE["member"].format(member, gdscript.name) +ERROR_TAIL
                )
                continue

        display_text, path = "", "../"
        if class_name:
            display_text, path = class_name, class_name
        if class_name and member:
            display_text+= "."
            path += "/"
        if member:
            display_text += member
            path += "#" + member.replace("_", "-")

        link: str = make_link(display_text, path)
        description = description.replace(reference,link, 1)
    return description



