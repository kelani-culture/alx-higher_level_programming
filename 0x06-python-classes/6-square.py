#!/usr/bin/python3

"""
    A program that print square
"""


class Square:
    """
        A class that print square with  space using '#'
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__postion

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError("Position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__size):
            if self.__postion[0] > 0 or self.__postion[1] == 0:
                print(" " * self.__postion[0], end="")
            for _ in range(self.__size):
                print('#', end="")
            print()
