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

    def area(self):
        ''' Evaluates the area of a rectangle object '''
        return self.__width * self.__height

    def __str__(self):
        ''' Print a formatted rectangle object '''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
