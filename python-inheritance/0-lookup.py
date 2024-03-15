#!/usr/bin/python3
""" defines an object attribut lookup function """


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)
