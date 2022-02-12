#!/usr/bin/python3
"""
Square class definition
"""

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        instanciation of a square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        get size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set size
        """
        self.__height = value
        self.__width = value

    def __str__(self):
        """
        returns object as a string
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))
