#!/usr/bin/python3
"""
a square class
"""


class Square:
    """
    Defines a Square and Accesses and updates a private Attribute
    """
    def __init__(self, size=0):
        """
        Initializes aSquare
        Attributes:
            __size(int): size of the size of a Square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        culculates Area of a Square
        """
        return (self.__size)**2
