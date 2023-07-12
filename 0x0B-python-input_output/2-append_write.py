#!/usr/bin/python3
'''
    Module contains a function to append to a text file
'''


def append_write(filename="", text=""):
    ''' Function to append to a text file '''
    with open(filename, 'a', encoding='utf-8') as f:
        appended_bytes = f.write(text)
        return appended_bytes
