#!/usr/bin/python3
"""
This module defines the Student class.

The Student class represents a student with attributes for first name,
last name, and age, and provides methods for JSON serialization and
deserialization.
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

        If attrs is a list of strings, only the attributes in this list
        are included. Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary containing selected attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): Dictionary containing attributes to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
