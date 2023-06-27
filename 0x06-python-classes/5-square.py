#!/usr/bin/python3

"""
    a program that print squares using the "#"
"""


class Square:
    """
        the class output the squares using '#'
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value == 0:
            print()
        self.__size = value

    def area(self):
        self.__size = self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
