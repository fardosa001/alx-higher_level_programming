#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, n in enumerate(row):
            if idx == len(row) - 1:
                print('{:d}'.format(n), end='')
            else:
                print('{:d}'.format(n), end=' ')
        print()
