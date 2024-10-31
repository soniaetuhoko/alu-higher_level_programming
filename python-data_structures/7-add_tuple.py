#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, use 0 for missing values
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Add the first and second elements of the tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
