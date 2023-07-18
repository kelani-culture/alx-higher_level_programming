#!/usr/bin/python3
"""
    A program that create a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        Initialize a new Rectangle instance.

        Parameters:
                width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
            TypeError: If x or y is not an integer.
            ValueError: If x or y is less than zero.
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
        """
            calculate area of shape
        """
        return self.__width * self.__height

    # display the rectangle shape
    def display(self):
        """
            display the shape using #
        """
        if self.__y > 0 and (self.__height and self.__width):
            for count in range(self.__y):
                print()
        for count in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            return string
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" +
                f" - {self.__width}/{self.__height}")

    # update the valuse of width, height, id, x, y
    def update(self, *args, **kwargs):
        """
            Update attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.height = args
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args
            elif len(args) == 5:
                self.id, self.width, self.height, self.x, self.y = args

        elif kwargs:
            if 'id' in kwargs.keys():
                self.id = kwargs.get('id')
            if 'height' in kwargs.keys():
                self.height = kwargs.get('height')
            if 'width' in kwargs.keys():
                self.width = kwargs.get('width')
            if 'x' in kwargs.keys():
                self.x = kwargs.get('x')
            if 'y' in kwargs.keys():
                self.y = kwargs.get('y')

    # return as dictionary
    def to_dictionary(self):
        """
            return attribut as dictionary
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
