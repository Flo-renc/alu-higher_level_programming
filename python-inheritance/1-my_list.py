#!/usr/bin/python3
""" class module """


class MyList(list):
    """ class my list"""
    def print_sorted(self):
        """ a method for sorting a list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
