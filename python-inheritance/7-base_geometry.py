# 7-base_geometry.py
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):  # Check if value is an integer
            raise TypeError(f"{name} must be an integer")
        if value <= 0:  # Check if value is greater than 0
            raise ValueError(f"{name} must be greater than 0")
