#!/usr/bin/python3
'''
    Module that contains a function to check if an
    instance of, or if the object is an instance of
    a class that is a subclass of the specified class
'''


def is_kind_of_class(obj, a_class):
    '''
    Function to check if an object is an instance of,
    or is an instance of a subclass of the specified class
    
    Arguments:
        obj: a given object
        a_class: a class type

    Returns:
        True: if the object is an instance of the specified class
        False: if the object is not an instance of the specified class
    '''
    return isinstance(obj, a_class)
