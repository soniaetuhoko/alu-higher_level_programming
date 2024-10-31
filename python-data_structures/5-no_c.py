#!/usr/bin/python3
def no_c(my_string):
    # Create a new string by iterating over the original string
    # and excluding characters 'c' and 'C'
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
