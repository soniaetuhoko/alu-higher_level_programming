#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each row's elements separated by a space
        print(" ".join("{:d}".format(x) for x in row))
