#!/usr/bin/python3
""" A program that define a class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Initialize a new Rectangle instance.

        Parameters:
            size (int): The size of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
            TypeError: If x or y is not an integer.
            ValueError: If x or y is less than zero.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # update square attribute
    def update(self, *args, **kwargs):
        """
            Update the square attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args

        elif kwargs:
            if 'id' in kwargs.keys():
                self.id = kwargs.get('id')
            if 'size' in kwargs.keys():
                self.size = kwargs.get('size')
            if 'x' in kwargs.keys():
                self.x = kwargs.get('x')
            if 'y' in kwargs.keys():
                self.y = kwargs.get('y')

    # return as dictionary
    def to_dictionary(self):
        """
            Write a to dictionary
        """
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
