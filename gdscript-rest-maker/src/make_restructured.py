"""General functions and utilities to write reStructured documents.
"""
from os import name
import re
import json
from dataclasses import dataclass
from typing import Dict, List, Any
import logging
from .config import LOG_LEVELS, LOGGER

api_ref = {}

with open("godot_api_calls.json", "r") as api_json:
    api_ref: list = json.loads(api_json.read())
    LOGGER.debug(
        "api_ref is {}".format(type(api_ref))
    )
    
@dataclass
class RestructuredDocument:
    title: str
    doc_ref: str
    content: List[str]

    def get_filename(self):
        return self.title + ".rst"

    def as_string(self) -> str:
        """
        Removes duplicate empty lines from the document and returns it as a
        string.
        """
        text: str = "\n".join(self.content)
        return re.sub(r"\n\n+", "\n\n", text)

    def __repr__(self):
        return "RestructuredDocument(title={}, doc_ref={} content={})".format(
            self.title, self.doc_ref,  "\\n".join(self.content)[:120] + "..."
        )


class RestructuredSection:
    def __init__(self, title: str, heading_level: int, content: List[str]):
        """
        Represents a section of a reStructured document.

        Keyword Arguments:
        title: str         --
        heading_level: int --
        content: List[str] -- content of the section
        """
        self.title: List[str] = make_heading(title, heading_level)
        self.content: List[str] = content

    def is_empty(self) -> bool:
        return not self.content

    def as_text(self) -> List[str]:
        return self.title + self.content if not self.is_empty() else []


def wrap_in_newlines(restructured: List[str] = []) -> List[str]:
    return ["", *restructured, ""]


def make_heading(line: str, level: int = 1) ->List[str]:
    """
    reStructured text headings are not well assigned but the convention
    followed is  
        # with overline, for parts

        \* with overline, for chapters
        
        = for sections
        
        - for subsections
        
        ^ for subsubsections
        
        " for paragraphs
    """

    level = 0 if level == 1 else 1

    heading_markers: List[str] = ["=", "-" ]
    heading_marker: str = heading_markers[level] * len(line)

    return ["", line, heading_marker, ""]


def escape_markdown(text: str) -> str:
    """Escapes characters that have a special meaning in markdown, like *_-"""
    # characters: str = "*_-+`"
    # for character in characters:
    #     text = text.replace(character, '\\' + character)
    # return text
    return text.translate(str.maketrans({
                                        "*": r"\*",
                                        "_": r"\_",
                                        "-": r"\-"
                                        }))


def make_bold(text: str) -> str:
    """Returns the text surrounded by **"""
    return "**" + text + "**"


def make_italic(text: str) -> str:
    """Returns the text surrounded by *"""
    return "*" + text + "*"


def make_code_inline(text: str) -> str:
    """Returns the text surrounded by `"""
    return "`" + text + "`"


def make_code_block(text: str, language: str = "gdscript") -> str:
    """Returns the text formatted as a reStructured code block """
    lines: List[str] = text.split("\n")
    code: str = "    " + "\n    ".join(lines)
    return "..  code-block:: {}\n\n{}\n".format(language, code)


def make_link(description: str) -> str:
    api_key: str = description.lower()
    if api_key in api_ref:
        LOGGER.info(
            "found ref, link is {}".format(api_ref[api_key])
        )
        return ":godot_class:`{} <{}>`".format(description, description.lower())
    else:
        link_target = "class_" + description.lower()
        return ":ref:`{} <{}>`".format(description, link_target)


def make_list(
    strings: List[str], is_numbered: bool = False, indent_level: int = 0
) -> List[str]:
    """Returns a bullet or ordered list from strings."""
    indent: str = "  " * indent_level

    def make_list_item(index: int, string: str) -> str:
        return indent + "{} {}".format(index + "." if is_numbered else "-", string)

    return [make_list_item(i, string) for i, string in enumerate(strings, start=1)]


def make_table_header(cells: List[str]) -> List[str]:
    return [make_table_row(cells), " --- |" * (len(cells) - 1) + " --- "]


def make_table_row(cells: List[str]) -> str:
    return " | ".join(cells)


def make_prop_table(props: List[str], class_name: str) -> List[str]:
    table_items: List[Dict] = []
    exp_length: int = 0
    type_length: int = 0
    name_length: int = 0
    default_length: int = 7
    for prop in props:
        prop_exported = "**export**" if prop.is_exported else ""
        prop_type: str = "var" if prop.type == "var" else make_link(prop.type)
        prop_name: str = ":ref:`{}<class_{}_property_{}>`".format(
                                                            prop.name.lower(),
                                                            class_name,
                                                            prop.name.lower()
                                                        )
        prop_def: str = "``{}``".format(prop.default_value) if prop.default_value else ""
        table_items.append({"exported": prop_exported, "type": prop_type, "name": prop_name, "default": prop_def})
    
    for item in table_items:
        e_len = len(item["exported"]) +2
        t_len = len(item["type"]) + 2
        n_len = len(item["name"]) + 2
        d_len = len(item["default"]) + 2
        if e_len > exp_length: exp_length = e_len
        if t_len > type_length: type_length = t_len
        if n_len > name_length: name_length = n_len
        if d_len > default_length: default_length = d_len

    table_separator: str = "+{}+{}+{}+{}+".format(
        "-" * exp_length, "-" * name_length, "-" * type_length, "-" * default_length
        )
    
    table: List[str] =[]
    table.append(table_separator)
    for row in table_items:
        item_row: str = "| {} | {} | {} | {} |".format(
                row["exported"] + " " * (exp_length - len(row["exported"]) - 2),
                row["name"] + " " * (name_length - len(row["name"]) - 2),
                (row["type"] + " " * (type_length - len(row["type"]) - 2)) if row["type"] is not "var " else " var ",
                row["default"] + " " * (default_length - len(row["default"]) - 2)
            )

        table.append(item_row)
        table.append(table_separator)

    return table


def make_func_table(funcs: List[str], class_name: str) -> List[str]:
    table_items: List[Dict] = []
    ret_type_len: int = 0
    func_call_len: int = 0

    for func in funcs:
        ret_type: str = None
        if func.return_type == "null" or func.return_type == "void":
            ret_type = func.return_type
        else:
            ret_type = make_link(func.return_type)
        func_call: List[str] = []
        func_call.append(":ref:`{}<class_{}_method_{}>` **(** ".format(
                                                    func.name,
                                                    class_name,
                                                    func.name.lower()
                                                    )
                                                )
        if func.arguments:
            for arg in func.arguments:
                arg_type: str = None
                arg_default: str = None
                if arg.type == "null" or arg_type == "void":
                    arg_type = arg.type
                else:
                    arg_type = make_link(arg.type)
                arg_default = " = {}".format(arg.default) if arg.default != "" else arg.default
                argument: str = "{}: {}{}".format(arg.name, arg_type, arg_default)

                func_call.append(argument)
                func_call.append(", ")
            func_call.pop() # get rid of the last comma
        
        func_call.append(" **)**")

        table_items.append({"func_call": ''.join(func_call), "ret_type": ret_type})

    for item in table_items:
        c_len = len(item["func_call"]) +2
        r_len = len(item["ret_type"]) + 2
        if c_len > func_call_len: func_call_len = c_len
        if r_len > ret_type_len: ret_type_len = r_len

    table_separator: str = "+{}+{}+".format(
        "-" * func_call_len, "-" * ret_type_len
        )
    
    table: List[str] =[]
    table.append(table_separator)
    for row in table_items:
        item_row: str = "| {} | {} |".format(
                row["func_call"] + " " * (func_call_len - len(row["func_call"]) - 2),
                row["ret_type"] + " " * (ret_type_len - len(row["ret_type"]) - 2)
            )

        table.append(item_row)
        table.append(table_separator)

    return table



def make_comment(text: str) -> str:
    """
    reSturctured text comment format -
    ..  This is a single line comment.

        And this continues the comment
    """
    lines: List[str] = text.split("\n")

    if len(lines) == 1:
        return "..  " + lines[0]
    else:
        return "..\n    " + "\n    ".join(lines)


def surround_with_html(text: str, tag: str) -> str:
    return "<{}>{}</{}>".format(tag, text, tag)
