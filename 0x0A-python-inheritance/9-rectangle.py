#!/usr/bin/python3

"""
    Base geometry class
"""


class BaseGeometry:
    """
        Base geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """
        Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # calculate area of rectangle
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
