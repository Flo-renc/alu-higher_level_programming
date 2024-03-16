#!/usr/bin/python3
""" class module """

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text, end='')
