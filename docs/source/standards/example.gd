# This is a dummy file for demonstrating the format of the
# commenting to provide automatic API documentation from Godot
#
# A comment at the start of the file is used a the description
# for the class and can have multiple sections provided the comment
# does not break as this comments is so far.
# 
# In order for the documentation to be generated the .gd file
# must have class_name defined

# The above blank line marks the end of the comments that will be 
# included in the API docs.

tool
extends Node2D
class_name api_doc_example  # This has to be defined for API inclusion

# Global properties can be documented using comments before the property
# This is a global boolean value
var a_global_boolean: bool = true;

# The gravity is a constant 
const GRAVITY :float = 9.81

# but be careful as the comment attaches to the next property
# and the order of property printing is not defined.
var property_d: int
var property_a: Vector2
var property_z: float 

# This is a function comment that will be included in the
# API docs as the comment block immediately precedes the
# function declaration.  All paramenters and return type 
# are also included.
#
# Function to print out a message in either upper of lower case
func hello_world(text: String, upper_case: bool) -> bool:
	
	# text string that will be printed
	var text2print:= ""
	
	# Have we altered the text
	var has_changed: bool = false
				
	if upper_case:
		text2print = text.to_upper()
	else:
		text2print = text.to_lower()
	
	print("Message was: ", text2print)
	
	has_changed = (text2print == text)
	
	return has_changed
	

# This function is commented but the comment will not be included
# as there is does not immediately proceed the funciton declaration

func add_two_digits(digit1: int, digit2: int) -> int:
	return digit1 + digit2
	
