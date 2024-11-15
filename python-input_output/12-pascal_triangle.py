#!/usr/bin/python3
"""
This module defines the pascal_triangle function.

The pascal_triangle function generates Pascal's triangle up to a given number
of rows, represented as a list of lists.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists, where each inner list represents a row
              of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
