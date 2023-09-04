#!/usr/bin/python3
def add_integer(a, b=98):
    """Addition function
    Attributes:
        a:first parameter could be an int or a float
        b:second parameter could be an int or a float
    Returns: sum of a and b
    Exceptions: 
        raises TypeError("a must be an integer or b must be an integer")

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return int(a + b)
    
