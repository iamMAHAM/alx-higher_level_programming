#!/usr/bin/python3
"""Module 11"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square representation"""
        msg = "[Square] {}/{}".format(self.__size, self.__size)
        return msg
