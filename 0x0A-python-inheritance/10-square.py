#!/usr/bin/python3
'''
    Module contains a square class that inherits
    class Rectangle's methods.
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Class that inherits the properties of Rectangle class
    '''
    def __init__(self, size):
        ''' Initializes a square instance '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        ''' Evaluates the area of a square object '''
        return self.__size ** 2
