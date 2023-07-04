#!/usr/bin/python3
"""
Module containing a rectangle class

The class has setter and getter methods for the
various instance variables: width and height respectively

"""


class Rectangle:
    """
    Defines a rectangle with width and height

    Each attributes has its setter and getter
    An appropriate exception is raised if the wrong type
    ... or value is provided for both width and height
    """
    __init__(self, width=0, height=0):
        '''
        Method to initialize an instance of a Rectangle.
        It defines two private attributes:
        width: int
                the width of the rectangle
        height: int
                the height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Returns the width of an instance of a Rectangle'''
        return self.__width

    @property
    def height(self):
        '''Returns the height of an instance of a Rectangle'''
        return self.__height

    @width.setter
    def width(self, value):
        '''
        Sets the width of a Rectangle instance

        value: int
                new value of the rectangle onject

        Exceptions:
        ----------
        Raise an exception when the value is not integer type
        Or the value is less than 0
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        '''
        Sets the height of the rectangle

        value: int
                new value of the rectangle object

        Exceptions:
        ----------
        Raises an exception when the value is not integer
        Or when the value is less than 0
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
