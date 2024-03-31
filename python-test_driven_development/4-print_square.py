#!/usr/bin/python3
""" Defines a function that prints a square with character # """


def print_square(size):
    """ prints square with character #.

    Args:
        size (length of square) that will determine the size of the square.

    Raises:
        TypeError: if is not integer. error: size must be integer
        TypeError: if if size is a float and is less than 0
        ValueError: if size is less than 0, size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
