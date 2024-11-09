#!/usr/bin/python3
"""Module that defines the Square class, which inherits from Rectangle."""

class BaseGeometry:
    """BaseGeometry class with area method and integer_validator."""
    
    def area(self):
        """Raises an Exception as area() is not implemented in BaseGeometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize width and height after validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class inheriting from Rectangle, with custom string output."""
    
    def __init__(self, size):
        """Initialize size after validation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"
