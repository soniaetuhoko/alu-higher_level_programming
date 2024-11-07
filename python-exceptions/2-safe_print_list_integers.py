#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Tracks the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count for each successful integer print
        except (ValueError, TypeError):
            continue  # Skip non-integer values silently
    print("")  # New line after printing all integers
    return count  # Return the number of integers printed
