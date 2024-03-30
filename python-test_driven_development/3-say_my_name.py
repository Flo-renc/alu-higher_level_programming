#!/usr/bin/python3
""" Module to define a name printing function """


def say_my_name(first_name, last_name=""):
    """ Print a name. 

    Args:
        first_name (str): The first anme to print.
        last_name (str): the last anme to print

    Raises:
        TypeError: if either first_anme or last_name are not strings
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}". format(first_name, last_name))
