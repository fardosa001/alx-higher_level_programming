#!/usr/bin/python3
"""Square class
A Square Class
"""


class Square:
    """
    Class Square definition
    """
    def __init__(self, size=0):
        """__init__

        Initializes a Square

        Attributes:
            __size(int): size value of a square,defaults to 0 if None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
