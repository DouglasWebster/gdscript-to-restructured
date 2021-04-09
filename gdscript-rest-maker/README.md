# GDScript reStructuredText Docs Maker

**gdscript2rest** is a tool to document your Godot gdscript files into ***re*****Structured*****Text*** (..rst) files and to create an index of the generated files if required.

The code is based on the [gdscript-docs-maker code](https://github.com/GDQuest/gdscript-docs-maker) from [**GDQuest**](https://www.gdquest.com/) and, in as far as the initial stages of the conversion are concerned, it is a direct copy of their code with a few notable exceptions:
- This version only provides ***re*****Structured*****Text*** (.rst) output - if you require markdown or Hugo output then please follow the above link and use the original version.
- As there is no facility to create markdown or Hugo files the `-f/--format` and  `-a/--author` options in the original are no longer available.
- Multi-line comments in the code are concatenated to single line comments unless there are multiple  line breaks, in which case the line breaks are preserved.  This is to give, hopefully, a better flow of the description text.

---
## Usage

A JSON file of the Godot projects docstrings has to be created first using either the ```generate-reference``` script on homepage or the original at [gdscript-docs-maker code](https://github.com/GDQuest/gdscript-docs-maker). Both locations have instructions on how to do this. 

Once the JSON file has been created then the reStructuredText documents can be created by running
```
python3 -m gdscript2rest $JSON-dump.json [options]
```
where $JSON-dump.json is the file created by ```generate-reference```.  

The above command will generate the files required and place them in a folder called export that is a sub folder of the Current Working Directory.  Calling:
Once the JSON file has been created then the reStructuredText documents can be created by running
```
python3 -m gdscript2rest -h
```

will give full program usage with detailing options tailoring the output location and generating an index file.

My Homepage has full instructions, a mini tutorial wiki's as well as a wiki on creating a Sphinx based webpage of your Games API.

Don't hesitate to raise issues or ask questions and if you like this tool then please spread the word!