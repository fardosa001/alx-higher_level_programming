#!/usr/bin/python3
"""module 0-add_integer"""


def add_integer(a, b=98):
    """Addition function
    Attributes:
        a:first parameter could be an int or a float
        b:second parameter could be an int or a float
    Return: sum of a and b
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


if __name__ == "__main__":
    print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
