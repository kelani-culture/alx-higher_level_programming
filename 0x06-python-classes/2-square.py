#!/usr/bin/python3

"""
     a class Square that defines a square by
"""


class Square:
    """
        check if a value is an integer
        or if a value is >= 0
    """

    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
