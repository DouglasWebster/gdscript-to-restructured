# Make links to the Godot API references

This is a small tool to create links to the Godot Help API's and store them as a JSON file in the following format:

```
{
    "animationplayer": "https://docs.godotengine.org/en/stable/classes/class_animationplayer.html", 
    "directionallight": "https://docs.godotengine.org/en/stable/classes/class_directionallight.html", 
    "joint2d": "https://docs.godotengine.org/en/stable/classes/class_joint2d.html",
    "collisionobject2d": "https://docs.godotengine.org/en/stable/classes/class_collisionobject2d.html",
    "physicsbody": "https://docs.godotengine.org/en/stable/classes/class_physicsbody.html",
    "visibilitynotifier2d": "https://docs.godotengine.org/en/stable/classes/class_visibilitynotifier2d.html",
       .
       .
       .
}
```
The Json file can then be used as a list, dictionary etc. to link the Godot class name with its associated help
page on the godot website.

## Prerequisites
The program relies upon the GhAPI library  and instructions for its installation and use are at https://ghapi.fast.ai

## Running the program

The program is small so can be run stand alone with:
* `python make-godot-api-refs/__main__.py ` <br/>

or by treating it as a module with 
* `python -m make-godot-api-refs`

using `python -m make-godot-api-refs -h` will result in 

```
usage: __main__.py [-h] [--token TOKEN] [--branch BRANCH] [-v] [--check-branches]

Given a godot-docs branch it scans the class folder and creates a JSON file linking the Godot class name with the API reference

optional arguments:
  -h, --help        show this help message and exit
  --token TOKEN     optional github access token (default "" may only gives 60 reads/hour)
  --branch BRANCH   optional branch for the class files (default: stable)
  -v, --verbose     Set the verbosity level. For example -vv sets verbosity to level 2. Default: 0.
  --check-branches  print out a list of the Godot document branches then exit without making the links
```

The output file will be `godot_api_calls.json` and will be placed in current working directory 






