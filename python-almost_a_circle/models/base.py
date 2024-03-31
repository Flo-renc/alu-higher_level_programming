#!/usr/bin/python3
"""
Module: base
Contains the Base class for managing id attribute.
"""

class Base:
    """
    Base class for managing id attribute.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of instances.
        id (int): Public instance attribute representing the identifier of the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with id.

        Args:
            id (int): Identifier for the object. Defaults to None.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
