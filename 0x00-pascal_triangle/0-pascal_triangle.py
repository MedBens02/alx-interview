#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
        returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        line = [1]
        for j in range(1, i):
            line.append(triangle[i-1][j-1] + triangle[i-1][j])
        line.append(1)
        triangle.append(line)

    return triangle
