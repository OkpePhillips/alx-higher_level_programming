#!/usr/bin/python3
'''
This Module contains a function to get the attributes
of an object
'''


def lookup(obj):
    ''' Returns a list of attributes for the object'''
    return dir(obj)
