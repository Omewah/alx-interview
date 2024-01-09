#!/usr/bin/python3
"""a script to represent Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    p_angle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(p_angle[i - 1][j - 1] + p_angle[i - 1][j])

        row.append(1)

        p_angle.append(row)

    return p_angle
