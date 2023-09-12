#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initializes class rectangle
        Args:
            __height(int): height
            __width(int): width

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """returns Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representantion"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
