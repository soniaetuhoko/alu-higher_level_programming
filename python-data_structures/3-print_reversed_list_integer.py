#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Iterate over the list in reverse order
    if my_list:
        for i in reversed(my_list):
            # Print each integer using str.format()
            print("{:d}".format(i))
