#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        new_matrix.append(list(map(lambda n: n**2, rows)))
    return (new_matrix)
