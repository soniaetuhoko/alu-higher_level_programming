#!/usr/bin/python3
"""
4-inherits_from.py

This module defines a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class;
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
