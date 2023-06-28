#!/usr/bin/python3
"""Module with init and area methods"""


class Square:
    """A square class with value and type validation as well
        as a public instance method called area"""
    def __init__(self, size=0):
        """Method to initialize a square object"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """A method to calculate the area of square object"""
        return self.__size ** 2
