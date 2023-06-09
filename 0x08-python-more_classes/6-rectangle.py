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

    A class attribute keeps track of number of instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
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
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''Returns the rectangle in the form of "#"'''
        if self.__width == 0 or self.__height == 0:
            rectangle = ''
        else:
            row = "#" * self.__width
            rectangle = (row + "\n") * self.__height
            rectangle = rectangle.rstrip("\n")
        return rectangle

    def __repr__(self):
        '''
        Returns a string representation of the rectangle to be able
        to recreate a new instance
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''
        Prints a message when a rectangle object is deleted.
        It also decrements the number of instances
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        '''Returns the area of a rectangle object'''
        area = self.__width * self.__height
        return area

    def perimeter(self):
        ''' Returns the perimeter of a rectangle object'''
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter
