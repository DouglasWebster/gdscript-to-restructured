# GDScript reStructuredText Docs Maker

This is a tool to document your Godot gdscript files into ***re*****Structured*****Text*** (..rst) files and to create an index of the generated files if required.

The code is based on the [gdscript-docs-maker code](https://github.com/GDQuest/gdscript-docs-maker) from [**GDQuest**](https://www.gdquest.com/) and, in as far as the initial stages of the conversion are concerned, it is a direct copy of their code with a few notable exceptions:
- This version only provides ***re*****Structured*****Text*** (.rst) output - if you require markdown or Hugo output then please follow the above link and use the original version.
- As there is no facility to create markdown or Hugo files the `-f/--format` and  `-a/--author` options in the original are no longer available.
- Multi-line comments in the code are concatenated to single line comments unless there are multiple  line breaks, in which case the line breaks are preserved.  This is to give, hopefully, a better flow of the description text.

## Installation

You should install gdscript2rest from [PyPI](https://pypi.org) with 

`python -m pip install gdscript2rest` 
 ## Additional requirements

In order to make the links from the Godot class names to the Godot API help files a link file has to be created and available to in the working directory of the program.  This can be accomplished by installing a small utility [godot-api-refs](https://pypi.org/project/godot-api-refs/) and running it in from the current working directory.

---
## Usage

There are 2 scripts in the repository:
* generate_reference     - for Linux and Mac (though the script is untested on a Mac)
* generate_reference.bat - for windows in a cmd prompt (it doesn't seem to work in a powershell terminal)

Both scripts will generate the documentation in the desired folder.

## Linux and Mac

Running `./generate_reference -h` in a terminal will give the following

```
    Generate reST file references from GDScript
    Usage:
    generate_reference $project_directory [options]

    Required arguments:

    $project_directory -- path to your Godot project directory.

    This directory or one of its subdirectories should contain a project.godot file.

    Options:

    -h/--help               Display this help message.
    -o/--output-directory   directory path to output the documentation into.
    -d/--directory          Name of a directory to find files and generate the code reference in
                            the Godot project. You can use the option multiple times to generate
                            a reference for multiple directories.
    -i/                     Create a reST index file in the output directory that references all
                            the API reST files.
    -v/--verbose            Set the verbosity level. For example -vv sets verbosity to level 2.
                            Defalt: 0.
    -V/--version            Print the version number and exit.
    --doc-version           Set the document version number if there is no version set in the
                            JSON file. Defaults to 0.0.0

    Usage example:

    generate_reference ~/Repositories/other/nakama-godot/project/ -o docs/source/api/addons 
              -d addons -i -v --doc-version 0.1.5

    This command walks files in the res://addons directory of the Godot Nakama project, and 
    stores the resultant code dump in the docs/source/api/addons directory of the current pwd.
    It then invokes gdscript2rest and creates the reST files in the same directory, detailing
    each file processed, creating an index file and setting the version to 0.1.5
```

## Windows

Running `generate_reference.bat -h` in a cmd window will give the following

```
Creates and parses reference documentation for a GDScript based projects.

generate_reference $Path [-p dest] [-v ^| -vv] [--dry-run] [-i] [-V] [--doc-version]

  $Path  The path to the Godot project.   

  -h --help           Display this help file.

  -p --path dest      Path to the output directory.
    
  -v --verbose        Set the verbosity level. For example, -vv sets the verbosity
                      level to 2.

  --dry-run           Run the script without actual rendering or creating files
                      and folders. For debugging purposes

  -i --make-index     If this flag is present, create an index.md page with a table
                      of contents.

  -V --version        Display the version of the gdscript2rest program

  --doc-version       Set the version number shown in the documentation.  Defaults to
                      0.0.0 (currently Godot does not output a version number).
```

The commands are the same as the Linux/Mac version except there is no option to cherry pick the directories in the Godot project.  This involves changing the ReferenceCollectorCLI.gd file on the fly which I something I don't know how to do in a batch file.

---
## Detailed explanation 

The generation of the ***re*****Structured*****Text*** files is a two step process.

1. Create a JSON file that contains all the information extracted from your Godot project script files.
2. Turn each of the separate classes in the JSON file that contains a class_name qualifier into a separate ***re*****Structured*****Text*** file.

The above script automates the two processes which can be accomplished individually by: 
## Stage 1 - Create the JSON file

This is done in the `generate_reference` script by:

1.  Copying the GDScript files `./godot-scripts/Collector.gd` and `./godot-scripts/ReferenceCollectorCLI.gd` or `./godot-scripts/ReferenceCollectorCLI.gd` to your Godot 3.3 project.
2. Running the GDScript code in the project with Godot
3. Removing the godot-scripts files that were initially copied over.

This leaves a copy of the ***reference.json*** file in the Godot project directory.

(The $project_directory and -d/--directory options are applicable to this stage)

A fuller explanation of this stage is detailed at  [gdscript-docs-maker code](https://github.com/GDQuest/gdscript-docs-maker) 

## Stage 2 - Create the reStructuredText documents

This is done in the `generate_reference` script by:

1. Moving the ***reference.json*** file from the Godot project directory to the output_directory, creating the output_directory if required
2. Running `python -m gdscript2rest $ReferenceFile [options]` where $ReferenceFile is the file created in part 1 and the options are the remaining unused options.  


## Detailed explanation of the gdscritp2rest python module

`gdscript2rest` is a python module that scans the reference.json file and creates individual reStructuredText files for each individual class enumerated in the file.  

The individual files have full linkages to:

* code inside the file i.e variable use in a function declaration to the variable declaration
* code in the same project i.e the parent class in a state machine.
* the Godot help system.  i.e. the declaration Extends: Node2D, the Node2d links to the Godot help file



If you run 
```
python -m gdscript2rest -h
```

it will display the following which lists the options available to the program.
```
usage: gdscript2rest [-h] [-p PATH] [-i] [-v] [--dry-run] [-V] files [files ...]

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
                        (For debugging purposes.)
  -V, --version         Print the version number and exit,
 --doc-version DOC_VERSION
                        Set the document version number if there is no version set in the JSON file. 
                        Defaults to 0.0.0
 ```

A fuller explanation of the options is:

* files :-> this is a list of files generated by ***generate-reference*** that is used as the input to the program
* -h --help :-> prints out the above usage statement and exits.
* -p PATH, --path PATH :-> outputs the reStructuredText files to PATH, this can be either an absolute or relative path
* -i :-> Creates an index file ***index.rst***.  This file is a very basic file with a single toctree entry that globs all the files in its directory
*  -v, --verbose :-> Prints out information as the program progresses.  Not over helpful but could aid in finding problems.
* --dry-run             Run the script at max verbosity without creating files. (For debugging purposes.)
*  -V, --version         Print the version number and exit,
* --doc-version DOC_VERSION :-> Unless I'm missing something Godot doesn't currently have the facility to store a version number so this gives the option to set the version number manually.  If not used the version number defaults to 0.0.0

---
## Further Information

For additional information and a brief tutorial on how to use the ***re*****Structured*****Text*** files to create a Sphinx documents site see the [Wiki](https://github.com/DouglasWebster/gdscript-to-restructured/wiki) section of this repository.

## Acknowledgements

My thanks to the people at [**GDQuest**](https://www.gdquest.com/) for providing the initial program from which this was derived and to the people at [Godot](https://godotengine.org/) for putting all there hard work out there for us to use.