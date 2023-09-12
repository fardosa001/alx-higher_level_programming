#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py):"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size):
        """Initializes square class)
        Args:
            __size(int): positive integer)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
