#!/usr/bin/python3

"""
    Rectangle program
"""


class Rectangle:
    """
        A class that defines a Rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # private instance attribute for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # private instance attribute for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # calculate area of rectangle
    def area(self):
        return self.__height * self.__width

    # calcualte perimeter
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    # print string representation
    def __str__(self):
        if self.__height <= 0 or self.__width <= 0:
            return ""
        rt = [[str(self.print_symbol) for _ in range(self.__width)]
              for _ in range(self.__height)]
        return "\n".join(["".join(row) for row in rt])

    def __repr__(self):
        return "Rectangle(2, 4)"

    # delete instances created
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # compare rectangles using area
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
