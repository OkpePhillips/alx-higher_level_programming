#!/usr/bin/python3
'''
    Module raises an exception for a class method
'''


class BaseGeometry:
    """ Class with a public instance method """
    def area(self):
        '''
        An umimplemented method that raises exception
        '''
        raise Exception("area() is not implemented")
