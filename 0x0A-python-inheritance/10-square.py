#!/usr/bin/python3
""" inherits from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    # calculate the area of a square
    def area(self):
        return super().area()

    def __str__(self):
        return super().__str__()
