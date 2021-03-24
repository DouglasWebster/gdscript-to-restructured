"""General functions and utilities to write reStructured documents.
"""
import re
import json
from dataclasses import dataclass
from typing import List, Any
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


def make_link(description: str, target: str) -> str:
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
