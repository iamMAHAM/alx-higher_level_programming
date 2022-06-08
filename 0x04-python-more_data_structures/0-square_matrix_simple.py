#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for mat in matrix:
        new_matrix.append(list(map(lambda x: x * x, mat)))

    return new_matrix
