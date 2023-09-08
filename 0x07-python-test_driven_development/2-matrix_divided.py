#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Attributes:
        __matrix(int, float): a list of lists of integers or floats
        __div(int, float): a number
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
       and all(isinstance(element, (int, float)) for element in row)
       for row in matrix):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2)
                   for element in row]
                  for row in matrix]
    return new_matrix
