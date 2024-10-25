#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the squared values
    return [[element ** 2 for element in row] for row in matrix]
