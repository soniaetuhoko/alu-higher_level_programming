#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1

    # Determine the correct wording for "argument" or "arguments"
    if num_args == 0:
        print("0 arguments.")
    else:
        arg_word = "argument" if num_args == 1 else "arguments"
        print(f"{num_args} {arg_word}:")

        # Print each argument with its position
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
