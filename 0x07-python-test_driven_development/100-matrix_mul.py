#!/usr/bin/python3

"""
    program to multiply matrix
"""


def matrix_mul(m_a, m_b):
    """
        Check for possible Errors
    """
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    else:
        if len(m_b) == 0:
            raise ValueError("m_b can't be empty")

    for list_1 in m_a:
        if len(list_1) == 0:
            raise ValueError("m_a can't be empty")
        if not isinstance(list_1, list):
            raise TypeError("m_a must be a list")

    for list_2 in m_b:
        if len(list_2) == 0:
            raise ValueError("m_b can't be empty")
        if not isinstance(list_2, list):
            raise TypeError("m_b must be a list")
    for idx, list_1 in enumerate(m_a):
        for idx, integer in enumerate(list_1):
            if (type(integer) is not int and type(integer) is not float):
                raise ValueError("m_a should contain only integers or floats")
        if idx < len(m_a):
            if len(m_a[0]) != len(m_a[idx]):
                raise TypeError("each row of m_a must be of the same size")

    for idx, list_2 in enumerate(m_b):
        for integer in list_2:
            if (type(integer) is not int and type(integer) is not float):
                raise ValueError("m_b should contain only integers or floats")
        if idx < len(m_b):
            if len(m_b[0]) != len(m_b[idx]):
                raise TypeError("each row of m_b must be of the same size")

    return mul_matrix(m_a, m_b)


def mul_matrix(m_a, m_b):
    """
        Multiply matrix
    """
    if len(m_a[0]) == len(m_b):
        a = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    a[i][j] = a[i][j] + m_a[i][k] * m_b[k][j]
    else:
        raise ValueError("m_a and m_b can't be multiplied")
    return a
