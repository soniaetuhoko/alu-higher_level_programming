#!/usr/bin/python3
"""
This module contains a function to return a JSON-like string representation of
a Python object.
It handles basic types such as lists, dictionaries, strings, integers, floats,
and booleans.

Functions:
    to_json_string(my_obj): Returns JSON-like string representation of Python
    object.
"""


def to_json_string(my_obj):
    """
    Returns JSON-like string representation of an object for basic data types

    Args:
        my_obj: The object to serialize to a JSON-like string.

    Returns:
        str: The JSON-like string representation of the object.
    """

    if isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, list):
        return "[" + ", ".join(to_json_string(item) for item in my_obj) + "]"
    elif isinstance(my_obj, dict):
        items = [
                to_json_string(key) + ": " + to_json_string(value)
                for key, value in my_obj.items()
                ]
        return "{" + ", ".join(items) + "}"
    else:
        raise TypeError(
            f"Object of type {type(my_obj).__name__} is not JSON serializable"
        )
