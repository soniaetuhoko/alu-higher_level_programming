#!/usr/bin/python3
"""
This module defines the say_my_name function.

The function prints 'My name is <first name> <last name>'.
Both first_name and last_name must be strings, otherwise it raises
a TypeError.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The first name, must be a string.
        last_name: The last name, must be a string (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
