#!/usr/bin/python3
""" class module """


class BaseGeometry:
    """ class """
    def area(self):
        """ to rasie an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
        self.name = name
        self.value = value