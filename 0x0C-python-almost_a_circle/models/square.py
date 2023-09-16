#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor
        Attributes:
            id:
            size(int):
            x:
            y:

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                self.x, self.y, self.size)
