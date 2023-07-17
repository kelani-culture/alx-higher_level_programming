#!/usr/bin/pyrhon3
"""
    A program that create a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        A rectangle class defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # private property setting for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # private property setting for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # private instance for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # private instance for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # calculate area of rectangle
    def area(self):
        return self.__width * self.__height

    # display the rectangle shape
    def display(self):
        if self.__y > 0 and (self.__height and self.__width):
            for count in range(self.__y):
                print()
        for count in range(self.__height):
            #end = "\n" if count != self.__width - 1 else ""
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" +
                f" - {self.__width}/{self.__height}")
