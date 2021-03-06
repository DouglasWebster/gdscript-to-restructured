..
    Auto-generated from JSON by GDScript restructured maker.
    Do not edit this document directly as all changes will be
    to be overwritten on the next auto-generation.

###############
api_doc_example
###############

**Extends:** `Node2D <../Node2D>`_

***********
Description
***********

This is a dummy file for demonstrating the format of the
commenting to provide automatic API documentation from Godot

A comment at the start of the file is used a the description
for the class and can have multiple sections provided the comment
does not break as this comments is so far.

In order for the documentation to be generated the .gd file
must have class_name defined

**********************
Constants Descriptions
**********************

GRAVITY
=======

..  code-block:: gdscript

    const GRAVITY: float = 9.81

The gravity is a constant

**********************
Propertry Descriptions
**********************

a_global_boolean
================

..  code-block:: gdscript

    var a_global_boolean: bool = true

Global properties can be documented using comments before the property
This is a global boolean value

property_d
==========

..  code-block:: gdscript

    var property_d: int

but be careful as the comment attaches to the next property
and the order of property printing is not defined.

property_a
==========

..  code-block:: gdscript

    var property_a: Vector2

property_z
==========

..  code-block:: gdscript

    var property_z: float

*******************
Method Descriptions
*******************

hello_world
===========

..  code-block:: gdscript

    func hello_world(text: String, upper_case: bool) -> bool

This is a function comment that will be included in the
API docs as the comment block immediately precedes the
function declaration.  All paramenters and return type
are also included.

Function to print out a message in either upper of lower case

add_two_digits
==============

..  code-block:: gdscript

    func add_two_digits(digit1: int, digit2: int) -> int

