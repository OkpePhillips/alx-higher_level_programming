#!/usr/bin/python3
class Square:
    """A class with getter and setter, as well as value and type validation
        for the size attribute"""
    def __init__(self, size=0):
        """Method to initialize a square object"""
        self.__size = size

    @property
    def size(self):
        """Method to get the size of a square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size of the square object"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """Method to calculate area of a square object"""
        return (self.__size ** 2)
