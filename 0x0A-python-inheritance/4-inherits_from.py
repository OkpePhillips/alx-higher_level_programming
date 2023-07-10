#!/usr/bin/python3
'''
    Module that contains a function to check if an
    object is a subclass of the specified class
'''


def inherits_from(obj, a_class):
    '''
    Function to check if an object is a subclass of the specified class
    
    Arguments:
        obj: a given object
        a_class: a class type

    Returns:
        True: if the object is a subclass of the specified class
        False: if otherwise
    '''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
