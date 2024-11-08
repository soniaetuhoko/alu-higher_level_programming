#!/usr/bin/python3
"""
Module 5-square.py
Defines a Square class with attributes, methods, and properties.
"""


class Square:
    """
    Represents a square with private instance attribute 'size'.
    Methods:
        - __init__(self, size=0)
        - area(self)
        - my_print(self)
    Properties:
        - size(self)
        - size(self, value)
    """

    def __init__(self, size=0):
        """
        Initializes a Square with an optional size.

        Args:
            size (int): Size of the square's sides (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring it is an integer and non-negative

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
