#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get the list of names defined in hidden_4
    names = dir(hidden_4)

    # Filter and sort names that do not start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Print each name on a new line
    for name in sorted(filtered_names):
        print(name)
