#!/usr/bin/python3
'''
    Module contains a Rectangle class that inherits
    BaseGeometry's methods.
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits the properties of BaseGeometry
    '''
    def __init__(self, width, height):
        ''' Initializesa rectangle instance '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
