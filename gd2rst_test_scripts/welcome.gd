# This is the main welcome screen for the project.
#
# It gathers the user information for later use.

extends Node

class_name Welcome

# The user's name
var user_name: String = ""
# The name the user's would like to be refered to
var user_handle: String = ""
# The user's age
var user_age: int = 0 

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
