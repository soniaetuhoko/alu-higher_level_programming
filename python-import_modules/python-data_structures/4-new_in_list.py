#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]

    # Check if the index is valid
    if idx >= 0 and idx < len(new_list):
        # Replace the element at the given index in the new list
        new_list[idx] = element

    # Return the new list, modified or not
    return new_list
