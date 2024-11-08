#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square instance with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
