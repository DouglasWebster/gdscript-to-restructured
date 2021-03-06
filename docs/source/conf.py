# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import sphinx_rtd_theme
import os
import sys

# -- Project information -----------------------------------------------------

project = 'Not Another Platformer'
copyright = '2021, Jonathan D Webster, Douglas S Webster'
author = 'Jonathan D Webster, Douglas S Webster'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# The full version, including alpha/beta/rc tags
version = '0.0.1'
release = version

pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

needs_sphinx = '3.0'

sys.path.append(os.path.abspath("_extensions"))

extensions = [
    'sphinx_tabs.tabs',
    "notfound.extension",
#    'm2r',
]

# Warning when the Sphinx Tabs extension is used with unknown
# builders (like the dummy builder) - as it doesn't cause errors,
# we can ignore this so we still can treat other warnings as errors.
sphinx_tabs_nowarn = True

# Custom 4O4 page HTML template.
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    "title": "Page not found",
    "body": """
        <h1>Page not found</h1>
        <p>
            Sorry, we couldn't find that page. It may have been renamed or removed
            in the version of the documentation you're currently browsing.
        </p>
        <p>
            If you're currently browsing the
            <em>latest</em> version of the documentation, try browsing the
            <a href="/en/stable/"><em>stable</em> version of the documentation</a>.
        </p>
        <p>
            Alternatively, use the
            <a href="#" onclick="$('#rtd-search-form [name=\\'q\\']').focus()">Search docs</a>
            box on the left or <a href="/">go to the homepage</a>.
        </p>
    """,
}

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:
    notfound_urls_prefix = ''

if not os.getenv("SPHINX_NO_GDSCRIPT"):
    extensions.append("gdscript")

# if not os.getenv("SPHINX_NO_SEARCH"):
#     extensions.append("sphinx_search.extension")

if not os.getenv("SPHINX_NO_DESCRIPTIONS"):
    extensions.append("godot_descriptions")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# You can specify multiple suffix as a list of string: ['.rst', '.md']
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'

# The master toctree document
master_doc = 'index'

# General information about the project
project = "Not Another Platformer"
copyright = (
    "2020 -2021, Jonathan Webster, Douglas Webster"
)
author = "Jonathan Webster, Douglas Webster"

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "latest")
# The full version, including alpha/beta/rc tags
release = version

# Parse Sphinx tags passed from RTD via environment
env_tags = os.getenv("SPHINX_TAGS")
if env_tags is not None:
    for tag in env_tags.split(","):
        print("Adding Sphinx tag: %s" % tag.strip())
        tags.add(tag.strip())  # noqa: F82

supported_languages = {
    "en": "Godot Engine (%s) documentation in English",
    "de": "Godot Engine (%s) Dokumentation auf Deutsch",
    "es": "Documentación de Godot Engine (%s) en español",
    "fr": "Documentation de Godot Engine (%s) en français",
    "fi": "Godot Engine (%s) dokumentaatio suomeksi",
    "it": "Godot Engine (%s) documentazione in italiano",
    "ja": "Godot Engine (%s)の日本語のドキュメント",
    "ko": "Godot Engine (%s) 문서 (한국어)",
    "pl": "Dokumentacja Godot Engine (%s) w języku polskim",
    "pt_BR": "Documentação da Godot Engine (%s) em Português Brasileiro",
    "ru": "Документация Godot Engine (%s) на русском языке",
    "uk": "Документація до Godot Engine (%s) українською мовою",
    "zh_CN": "Godot Engine (%s) 简体中文文档",
    "zh_TW": "Godot Engine (%s) 正體中文 (台灣) 文件",
}

language = os.getenv("READTHEDOCS_LANGUAGE", "en")
if not language in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong, or it should be added to supported_languages in conf.py. Falling back to 'en'."
    )
    language = "en"

is_i18n = tags.has("i18n")  # noqa: F821

exclude_patterns = ["_build"]

# fmt: off
# These imports should *not* be moved to the start of the file,
# they depend on the sys.path.append call registering "_extensions".
# GDScript syntax highlighting
from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers["gdscript"] = GDScriptLexer()
# fmt: on

smartquotes = False

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"
highlight_language = "gdscript"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']
html_extra_path = ["robots.txt"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
    "css/my.css"
]

html_js_files = [
    "js/custom.js",
]

html_theme_options = {
    'logo_only': True,
    'collapse_navigation': False
}

latex_elements = {
    'extraclassoptions': 'openany',
    'preamble': r'''
\usepackage{subfig}
\usepackage{graphicx}
''',
    'papersize': 'a4paper'
}
