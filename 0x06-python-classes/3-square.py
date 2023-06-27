#!/usr/bin/python3

"""
     a class Square that calculates the area of a square
"""


class Square:
    """
        check if a value is an integer
        or if a value is >= 0
        return: the area
    """

    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
