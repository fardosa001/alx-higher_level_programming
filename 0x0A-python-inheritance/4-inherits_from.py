#!/usr/bin/python3
def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    Args:
        obj: object
        a_class: class
    Returns:
        True if the object is an instance of a class that inherited from.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
