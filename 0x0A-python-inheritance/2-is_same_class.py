#!/usr/bin/python3
"""returns True if the object is exactly an instance
of the specified class; otherwise False."""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a specified class.
    Args:
        obj: object to be checked
        a_class(class): class to compare
    Returns:
        True if obj is exactly an instance of specified class otherwise False
    """
    return type(obj) is a_class
