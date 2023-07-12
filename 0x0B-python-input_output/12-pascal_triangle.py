#!/usr/bin/python3

"""
    pascal triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1 if j == 0 else j for j in range (i)] for i in range(1, n + 1)]
    for i in range(1, len(pascal)):
        for j in range(1, i + 1):
            if j == len(pascal[i]) - 1:
                pascal[i][j] = 1
            else:
                pascal[i][j] = empty[i - 1][j - 1] + empty[i - 1][j + 2 - 2]
    return pascal
