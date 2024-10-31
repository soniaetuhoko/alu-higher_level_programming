#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Use slicing to delete the element at the specified index
        my_list[idx:idx + 1] = []  # This deletes the item at index idx

    return my_list
