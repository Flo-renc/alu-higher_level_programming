#!/usr/bin/python3
""" class module """


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
            return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            print(0)
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width] * self.__height)
