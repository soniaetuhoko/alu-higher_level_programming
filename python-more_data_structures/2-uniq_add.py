#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set from the list to ensure uniqueness
    # and then sum the unique integers
    unique_integers = set(my_list)
    return sum(unique_integers)
