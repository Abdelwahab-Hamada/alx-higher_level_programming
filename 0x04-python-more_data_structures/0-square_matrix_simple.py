#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_matrix.append(list(map(lambda col: col ** 2, row)))

    return (new_matrix)
