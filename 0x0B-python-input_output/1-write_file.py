#!/usr/bin/python3
'''
    Module containing a function to write a string
    to file
'''


def write_file(filename="", text=""):
    '''Function to write string to file'''
    with open(filename, "w", encoding='utf-8') as f:
        bytes_written = f.write(text)
        return bytes_written
