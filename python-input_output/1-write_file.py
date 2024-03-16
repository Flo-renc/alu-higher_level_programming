#!/usr/bin/python3
""" class module """


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8) and returns the number of characters written:"""
    with open(filename , 'w', encoding='utf-8') as file:
        text = file.write(text)
        return (text)
