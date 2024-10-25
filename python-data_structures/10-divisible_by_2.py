#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list with True or False depending on divisibility by 2
    return [num % 2 == 0 for num in my_list]
