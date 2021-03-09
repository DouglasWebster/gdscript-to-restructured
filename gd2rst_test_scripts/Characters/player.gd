# This is the base class for all  characters in the game.
# 
# Only basic information is required for the base classs 
# and characters should be created from the derived classes
# where the characters can have thier own relevant attributes
class_name Character

extends KinematicBody

# A chararcter can be in one of three possible states.
# As well as the binary states of alive and dead a
# character can also be in limbo i.e. neither alive or
# dead
enum State {
	ACTIVE = 0,
	DEAD = 1,
	IN_LIMBO =2,
}

# 0:100 - a measure of how fast the character recovers
var health: int
# a measure of how fast the 
var strength: int


# on_created should be used to register a character
# This will fail if the character name has already
# been allocated. 
func _on_created(name: String) -> bool:
	if name.length() > 0:
		return true
	else:
		return false

# If the characater can be resurected it enters limbo
# otherwise it is dead
func _on_killed():
	pass


# The damage a character suffers is taken off
# the health.  Limit the removal of health to 0
func _on_damage(damage: int) -> int:
	health -= damage
	if health < 0:
			health = 0 
	return health
	
	
func _ready():
	pass
