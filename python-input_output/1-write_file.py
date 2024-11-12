#!/usr/bin/python3
"""
This module contains a function to write a string to a UTF-8 encoded text file.
The function writes a specified text to a file, creating or overwriting file
as needed.

Functions:
    write_file(filename="", text=""): Writes a string to a file and returns the
    number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoding) and returns the number of
    characters written.
    If the file does not exist, it will be created. If it does exist, content
    will be overwritten.

    Args:
        filename (str): The name of the file to write to. Default is an empty
        string.
        text (str): The string to write to the file. Default is an empty string

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
