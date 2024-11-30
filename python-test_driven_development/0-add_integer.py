#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers (or floats) a and b and returns the result as an integer.
    a and b must be integers or floats, otherwise raises TypeError.
    """
    # Check if 'a' is an integer or float, otherwise raise TypeError
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if 'b' is an integer or float, otherwise raise TypeError
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast 'a' and 'b' to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b

