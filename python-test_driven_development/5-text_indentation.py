#!/usr/bin/python3
""" defines a function that prints a text with 2 new lines """


def text_indentation(text):
    """ a function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text must be a string

    Raises:
        TypeError: if text is not string. error message text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    lines = []
    line = ""
    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            line = ""
    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
