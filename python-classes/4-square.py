#!/usr/bin/python3
""" class module """
class Square:
    """ presenting class square """


    def __init__(self, size=0):
        """ constructor method """
        self.size = size  # Call the setter method to set the size

    @property
    def size(self):
        """ propety """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter to set conditions for size type """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ get current area """
        return self.__size ** 2
