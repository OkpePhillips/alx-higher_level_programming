#!/usr/bin/python3
'''
    Module contains a function that checks if an object
    is an instance of a given class
'''


def is_same_class(obj, a_class):
    '''
    Function checks if an object is an instance of
    a given class.

    Arguments:
        obj: an object
        a_class: class type

    Return:
        True: if obj is an instance
        False: if otherwise
    '''
    return type(obj) is a_class
