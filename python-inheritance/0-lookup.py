#!/usr/bin/python3
"""
0-lookup.py

This module defines the lookup function that returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the object's attributes
        and methods.
    """
    return dir(obj)
