#!/usr/bin/python3
"""Module 12"""


def pascal_triangle(n):
    """Calculate n triangle pascal"""
    triangle = []
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)

        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        if(len(triangle) > 1):
            triangle[i].append(1)

    return triangle
