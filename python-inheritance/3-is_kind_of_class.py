#!/usr/bin/python3
"""
3-is_kind_of_class.py

This module defines a function to check if an object is an instance of,
or if it is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a class that inherited from
        a_class; False otherwise.
    """
    return isinstance(obj, a_class)
