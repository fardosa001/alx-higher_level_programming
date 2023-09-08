#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """prints a square
    Attributes:
        __size(int): size length of the square

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for rows in range(size):
            print('#' * size)
