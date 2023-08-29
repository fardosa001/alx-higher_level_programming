#!/usr/bin/python3
"""Square class
Defines a square with a private instance attribute
"""


class Square:

    def __init__(self, size=0):
        """__init__
        Initializes the size value of a Square.

        Attributes:
            __size(int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
