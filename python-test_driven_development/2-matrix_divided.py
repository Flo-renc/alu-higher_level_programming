#!/usr/bin/python3
""" Module """


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix
    
    Arguments must be float or int for both matrix and div
    Raise:
        TypeError: matrix must be a list of lists of integers or floats
        and div must be a number (integer or float)"""
    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix)
            or not all((isinstance(ele, int) or isintance(ele, float)) for ele in [num for row in matrix
                for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([listmap(lambda x: round(x / div, 2), row)) for row in matrix])
