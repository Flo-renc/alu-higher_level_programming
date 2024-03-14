#!/usr/bin/python3
""" class module """

class Rectangle:
    """ presenting class rectangle """
    def __init__(self, width=0, height=0):
        """ constructor method """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(width, int):
                raise TypeError("width must be an intenger")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        def height(slef, value):
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError(" height must be >= 0")
            self.__hieght = value


