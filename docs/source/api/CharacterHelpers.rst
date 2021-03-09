..
    Auto-generated from JSON by GDScript restructured maker.
    Do not edit this document directly as all changes will be
    to be overwritten on the next auto-generation.

################
CharacterHelpers
################

**Extends:** `Node <../Node>`_

***********
Description
***********

This has general helper and bookeeping methods for the characters
It holds the charactes in the game and can be interogated
to supply information between characters

**********************
Propertry Descriptions
**********************

characters
==========

..  code-block:: gdscript

    var characters: Dictionary

A list of characters and an associated id

last_id
=======

..  code-block:: gdscript

    var last_id: int = 1

a unique id for each character

*******************
Method Descriptions
*******************

add_character
=============

..  code-block:: gdscript

    func add_character(name: String) -> bool

Check if a character name is already in use and
if so return false.  If not register the character
and allocate an id.

get_id
======

..  code-block:: gdscript

    func get_id(name: String) -> int

Get the character ID if the character exists
a return value of -1 indicates no character

_on_signal_get_ID
=================

..  code-block:: gdscript

    func _on_signal_get_ID(name: String) -> int

access the character ID's through signals