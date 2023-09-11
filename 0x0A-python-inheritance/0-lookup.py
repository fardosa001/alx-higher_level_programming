#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns a list object
    Args:
    obj(object): The object

    Returns:
    list: list of attributes and methods

    """
    return dir(obj)
