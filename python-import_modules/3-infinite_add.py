#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize a variable to hold the sum
    total = 0

    # Loop through the arguments and add them to total
    for arg in sys.argv[1:]:
        total += int(arg)

    # Print the total sum
    print(total)
