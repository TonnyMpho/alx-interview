#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ function to return the pascal triangle matrix/ list of lists """
    if n <= 0:
        return []

    matrix = [[1]]

    for i in range(1, n):
        values = [1]
        for j in range(1, i):
            values.append(matrix[i-1][j-1] + matrix[i-1][j])
        values.append(1)
        matrix.append(values)

    return matrix
