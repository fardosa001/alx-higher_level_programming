#!/usr/bin/python3
"""
a square class
"""


class Square:
    """
    Square class defination
    """
    def __init__(self, size=0):
        """
        Initializes Square

        Attributes:
            __size(int): size value of the Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates Area of a Square
        """
        return (self.__size)**2
