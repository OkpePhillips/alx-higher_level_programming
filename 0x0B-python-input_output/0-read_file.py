#!/usr/bin/python3

'''
    This module contains a function to read file
    and print it to stdout
'''


def read_file(filename=""):
    '''Function to read file and print to stdout '''

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
