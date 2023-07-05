#!/usr/bin/python3

"""
    program that add two integer
    integers number together
"""


def add_integer(a, b=98):
    """
        for add ing integers
        Return: sum of integers
    """
    if isinstance(a, int) is not True and isinstance(a, float) is not True:
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and isinstance(b, float) is not True:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
