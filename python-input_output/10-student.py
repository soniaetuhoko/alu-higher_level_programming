#!/usr/bin/python3
"""
Module for the Student class.

This module defines a Student class with public instance attributes for
first name, last name, and age, and a method to retrieve a dictionary
representation of the instance.
"""


class Student:
    """
    Defines a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: A dictionary with the student's selected attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
