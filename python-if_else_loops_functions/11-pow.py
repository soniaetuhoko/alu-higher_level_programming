#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1  # Any number raised to the power of 0 is 1
    elif b < 0:
        return 1 / (a ** (-b))  # Handle negative powers
    else:
        result = 1
        for _ in range(b):
            result *= a  # Multiply a, b times
        return result
