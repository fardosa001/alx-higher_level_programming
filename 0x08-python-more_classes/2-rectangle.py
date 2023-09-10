#!/usr/bin/python3
"""module 2-rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes  a rectangle
        Attributes:
            width(int): width of rectancle
            height(int): height of rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectancle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
