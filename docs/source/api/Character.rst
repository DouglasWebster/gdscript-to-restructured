..
    Auto-generated from JSON by GDScript restructured maker.
    Do not edit this document directly as all changes will be
    to be overwritten on the next auto-generation.

#########
Character
#########

**Extends:** `KinematicBody <../KinematicBody>`_

***********
Description
***********

This is the base class for all  characters in the game.

Only basic information is required for the base classs
and characters should be created from the derived classes
where the characters can have thier own relevant attributes

************
Enumerations
************

State
=====

..  code-block:: gdscript

    const State: Dictionary = {"ACTIVE":0,"DEAD":1,"IN_LIMBO":2}

A chararcter can be in one of three possible states.
As well as the binary states of alive and dead a
character can also be in limbo i.e. neither alive or
dead

**********************
Propertry Descriptions
**********************

health
======

..  code-block:: gdscript

    var health: int

0:100 - a measure of how fast the character recovers

strength
========

..  code-block:: gdscript

    var strength: int

a measure of how fast the

*******************
Method Descriptions
*******************

_on_created
===========

..  code-block:: gdscript

    func _on_created(name: String) -> bool

on_created should be used to register a character
This will fail if the character name has already
been allocated.

_on_killed
==========

..  code-block:: gdscript

    func _on_killed()

If the characater can be resurected it enters limbo
otherwise it is dead

_on_damage
==========

..  code-block:: gdscript

    func _on_damage(damage: int) -> int

The damage a character suffers is taken off
the health.  Limit the removal of health to 0