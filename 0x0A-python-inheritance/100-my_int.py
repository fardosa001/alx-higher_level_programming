#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class that inherits int"""
    def __eq__(self, num):
        """returns opposite of __eq__"""
        return super().__ne__(num)

    def __ne__(self, num):
        """returns opposite of__ne__"""
        return super().__eq__(num)
