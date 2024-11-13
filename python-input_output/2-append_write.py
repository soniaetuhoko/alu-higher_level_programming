#!/usr/bin/python3
"""
This module contains a function to append a string to a UTF-8 encoded text file
The function appends specified text to the end of a file, creating the file if
it does not exist.

Functions:
    append_write(filename="", text=""): Appends a string to a file and returns
    the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8 encoding) and returns the number of
    characters added.
    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to append to. Default is an empty
        string.
        text (str): The string to append to the file. Default is empty string

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
