#!/usr/bin/python3
"""
Square class
"""


class Square:
    """Square class
    Square class Defination
    """
    def __init__(self, size=0):
        """
        Initializes a Square
        Attributes:
            __size(int): size of the side os a square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculates area of a square
        """
        return (self.__siz)**2

    def my_print(self):
        """
        prints square with character #
        """
        if self.__size == 0:
            print("")
            return None

        for rows in range(self.__size):
            print("#" * (self.__size))
