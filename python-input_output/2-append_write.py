#!/usr/bin/python3
""" class """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added."""
    # Open the file in append mode ('a+') which creates the file if it doesn't exist
    with open(filename, 'a+', encoding='utf-8') as file:
        # Get the current position in the file to track the number of characters added
        start_position = file.tell()
        # Append the text to the file
        file.write(text)
        # Calculate the number of characters added by subtracting the starting position from the current position
        num_characters_added = file.tell() - start_position
    return num_characters_added
