#!/usr/bin/python3
# 7-main.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# Valid cases
bg.integer_validator("my_int", 12)  # This will pass without error
bg.integer_validator("width", 89)  # This will pass without error

# Invalid cases
try:
    bg.integer_validator("name", "John")  # Raises TypeError: name must be an integer
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)  # Raises ValueError: age must be greater than 0
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)  # Raises ValueError: distance must be greater than 0
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
