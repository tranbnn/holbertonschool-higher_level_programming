#!/usr/bin/env python3

def square_matrix_simple(matrix=[]):

    new_list = []

    for row in matrix:
        squared_matrix = map(lambda x: x * x, row)
        new_list.append(list(squared_matrix))

    return new_list
