#!/usr/bin/python3
""" class """


def append_write(filename="", text=""):
    """end of file and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
