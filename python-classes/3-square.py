#!/usr/bin/python3
""" class module """

class Square:
    """ presenting class Square"""

    def __init__(self, size=0):
        """constructor method set size to 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ a public instance that returns the current error """
        return self.__size ** 2
