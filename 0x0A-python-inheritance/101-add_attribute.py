#!/usr/bin/python3
"""adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object
    Args:
        obj: object
        attr: attribute
        value: value

    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
