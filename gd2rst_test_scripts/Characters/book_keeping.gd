# This has general helper and bookeeping methods for the characters
# It holds the charactes in the game and can be interogated
# to supply information between characters

class_name CharacterHelpers

extends Node
# A list of characters and an associated id
var characters: Dictionary = {}
# a unique id for each character
var last_id: int = 1

# Check if a character name is already in use and 
# if so return false.  If not register the character
# and allocate an id.
func add_character(name: String) -> bool:
	var character_added = false
	if not name in characters:
		characters[name] = last_id
		last_id += 1
		character_added = true

	return character_added
		

# Get the character ID if the character exists
# a return value of -1 indicates no character
func get_id(name: String) -> int:
	if name in characters:
		return characters[name]
	else:
		return -1
		

func _ready():
	pass
	

# access the character ID's through signals
func _on_signal_get_ID(name: String) -> int:
	return get_id(name)
		
