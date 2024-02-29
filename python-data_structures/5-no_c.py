#!/usr/bin/python3


def no_c(my_string):
    """Remove all occurrences of 'c' and 'C' from the string."""
    result = ""
    for char in my_string:
        if char.lower() != 'c' and char.upper != 'C':
            result += char
    return result
