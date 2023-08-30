#!/usr/bin/python3
"""Square class
Defines a Square
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        Initializes a Square

        Attributes:
            __size(int): size value of a square
        """
        if type(size) is not (int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__self = size
