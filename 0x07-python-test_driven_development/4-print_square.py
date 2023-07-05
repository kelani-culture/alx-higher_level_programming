#!/usr/bin/python3

"""
    program that print square using '#'
"""


def print_square(size):
    """
        boring function for printing square with '#'
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for __ in range(size):
            print('#', end="")
        print()
