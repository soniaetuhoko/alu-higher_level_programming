#!/usr/bin/python3
"""
6-base_geometry.py

This module defines a BaseGeometry class with an area method.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Method that raises an Exception for unimplemented area."""
        raise Exception("area() is not implemented")
