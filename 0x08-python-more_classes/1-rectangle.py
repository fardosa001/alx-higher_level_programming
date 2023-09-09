#!/usr/bin/python3
"""A class rectangle"""


class Rectangle:
    """Defines a class rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle
         Attributes:
            __width(int): width of the rectangle
            __height(int): height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
