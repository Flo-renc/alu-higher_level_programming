#!/usr/bin/python3
"""class module """


def is_kind_of_class(obj, a_class):
    """ to check if an instance is an object of a superclass and a subclass """
    return isinstance(obj, a_class)
#he function first checks if the object is an instance of the specified class using isinstance(obj, a_class), which accounts for inheritance. 
