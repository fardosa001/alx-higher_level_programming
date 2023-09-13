#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n(int): integer value
    """
    if n <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        next_row = [1]
        prev_row = p_triangle[-1]

        for k in range(1, i):
            next_elem = prev_row[k - 1] + prev_row[k]
            next_row.append(next_elem)

        next_row.append(1)
        p_triangle.append(next_row)

    return p_triangle
