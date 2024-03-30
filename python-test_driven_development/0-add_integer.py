#!/usr/bin/python3
""" Module """

def add_integer(a, b=98):
    """ a function to add intergers a and b

    float arguments are typecast to int before
    addition is performed.

    Raises: 
        TypeError: if either a and b is of non-integer or 
        non-float.
        """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError(" a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

