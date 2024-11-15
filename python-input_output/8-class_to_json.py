#!/usr/bin/python3
"""
Module for class_to_json function.

This function returns a dictionary description with a simple data structure
(list, dictionary, string, integer, or boolean) for JSON serialization of
an object's attributes.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object.

    Args:
        obj: An instance of a class containing attributes that are lists,
             dictionaries, strings, integers, or booleans.

    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
