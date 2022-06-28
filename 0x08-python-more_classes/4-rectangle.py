#!/usr/bin/python3

"""Class for an empty rectangle"""


class Rectangle:
    """this is a rectangle class"""

    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")

        if (type(height) != int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the representation of a rectangle Objects"""

        w = self.__width
        h = self.__height
        rect = ""
        if (self.perimeter() != 0):
            for i in range(self.__height):
                rect = "{}{}".format(('#' * w + '\n') * (h - 1), '#' * w)
        return rect

    def __repr__(self):
        """Representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)
