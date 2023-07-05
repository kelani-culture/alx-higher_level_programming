#!/usr/bin/python3

"""
    A program that divides an integer array
"""


def matrix_divided(matrix, div):
    """
        A function that divides a matrix of integer
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for list_ in matrix:
        if isinstance(list_, list) is not True:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for value in list_:
            if (not isinstance(value, int)) and (not isinstance(value, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    for idx in range(len(matrix) - 1):
        if len(matrix[idx]) != len(matrix[idx + 2 - 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    div = [[round(j / div, 2) for j in num] for num in matrix]
    return div
