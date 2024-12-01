#!/usr/bin/python3
"""
This module defines the print_square function.

The function prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square, must be an integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
