#!/usr/bin/python3
""" class module """


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class."""
    return type(obj) == a_class
