#!/usr/bin/python3
lookup = __import__('0-lookup').lookup
"""class module """


class MyClass1(object):
    """class Myclass1"""
    pass
"""class module """


class MyClass2(object):
    """ class Myclass """
    my_attr1 = 3

    def my_meth(self):
        """ method """
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
