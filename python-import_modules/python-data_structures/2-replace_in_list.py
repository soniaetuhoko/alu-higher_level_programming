#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if the index is within valid range
    if idx >= 0 and idx < len(my_list):
        # Replace the element at the given index
        my_list[idx] = element
    # Return the original list (modified or not)
    return my_list
