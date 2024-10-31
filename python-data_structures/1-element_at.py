#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
