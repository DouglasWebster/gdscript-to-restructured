Coding Standards
----------------

The coding for the game will follow the standard recommended by the `Godot Style Guide <https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_styleguide.html>`_ with the following additions to enable automatic API generation.

Inclusion in the API build.
===========================

For a Godot script file to be included in the API build it must have the class name defined.  If this is defined then all properties, classes and functions within the class will be documented.

There is no special format for the documentation as it solely relies upon comments in the code.  These comments should immediately proceed the item being commented upon.  The comments can span multiple lines and have blank lines provided it is a blank comment line.  A comment that is followed by a blank line will not be included in the documentation.

.. note::
    Comment inside a function are not included in the documentation as the internals of a function should not be exposed to the outside world.
    

The following is an example of how comments attach to the items and the resulting API documentation layout
 
.. code::

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
    # as it does not immediately proceed the function declaration

    func add_two_digits(digit1: int, digit2: int) -> int:
	return digit1 + digit2
	


.. raw:: html

   <!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->



api_doc_example
===============

**Extends:** `Node2D <../Node2D>`_

Description
-----------

This is a dummy file for demonstrating the format of the
commenting to provide automatic API documentation from Godot

A comment at the start of the file is used a the description
for the class and can have multiple sections provided the comment
does not break as this comments is so far.

In order for the documentation to be generated the .gd file
must have class_name defined

Constants Descriptions
----------------------

GRAVITY
^^^^^^^

.. code-block:: gdscript

   const GRAVITY: float = 9.81

The gravity is a constant

Property Descriptions
---------------------

a_global_boolean
^^^^^^^^^^^^^^^^

.. code-block:: gdscript

   var a_global_boolean: bool = true

Global properties can be documented using comments before the property
This is a global boolean value

property_d
^^^^^^^^^^

.. code-block:: gdscript

   var property_d: int

but be careful as the comment attaches to the next property
and the order of property printing is not defined.

property_a
^^^^^^^^^^

.. code-block:: gdscript

   var property_a: Vector2

property_z
^^^^^^^^^^

.. code-block:: gdscript

   var property_z: float

Method Descriptions
-------------------

hello_world
^^^^^^^^^^^

.. code-block:: gdscript

   func hello_world(text: String, upper_case: bool) -> bool

This is a function comment that will be included in the
API docs as the comment block immediately precedes the
function declaration.  All paramenters and return type
are also included.

Function to print out a message in either upper of lower case

add_two_digits
^^^^^^^^^^^^^^

.. code-block:: gdscript

   func add_two_digits(digit1: int, digit2: int) -> int
