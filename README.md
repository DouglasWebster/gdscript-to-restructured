# GDScript reStructured Docs Maker

This is a set of tools to convert documentation written in your Godot gdscript files into reStructured (..rst) files

The .rst files will be formatted to mimic the style of code formatting shown in the Godot online manual API pagers.

This relies heavily on the [gdscript-docs-maker code](https://github.com/GDQuest/gdscript-docs-maker) from [**GDQuest**](https://www.gdquest.com/) and, in as far as the initial stages of the conversion are concerned, it is a direct copy of their code with a few notable exceptions:
- This version only provides reStructured (.rst) output - if you require markdown of Hugo output the please follow the above link and use the original version.
- As there is no facility to create markdown or Hugo files the `-f/--format` and  `-a/--author` options in the original are no longer available.

## Installation

This is an initial version of the project and at the moment generates files with the same look and feel as the .md files generated by the original [**GDQuest**](https://www.gdquest.com/) program.  It is strongly recommended that you use the original version from GDQuest to generate your documentation and then use a .md to .rst convertor to create your reStructured documents.

If you wish to try it out then follow the instructions at [GDQuest gdscript-docs-maker](https://github.com/GDQuest/gdscript-docs-maker/tree/master/godot-scripts) to generate the json file (default is reference.json) then generate the .rst documents by running the following from the command line:
```
python -m gdscript-rest-maker reference.json
```

for information on the use run 
```
python -m gdscript-rest-maker -h
```
which should display
```
usage: gdscript-rest-maker [-h] [-p PATH] [-i] [-v] [--dry-run] [-V] files [files ...]

Converts JSON data dumped by Godot's GDScript language server to create .rst files for 
use with Sphinx.

positional arguments:
  files                 A list of paths to JSON files.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the output directory.
  -i, --make-index      If this flag is present, create an index.rst page with a table of contents.
  -v, --verbose         Set the verbosity level. For example -vv sets verbosity to level 2. 
                        (Default: 0.)
  --dry-run             Run the script at max verbosity without creating files.
                        (For debuggin puposese.)
  -V, --version         Print the version number and exit,
  ```