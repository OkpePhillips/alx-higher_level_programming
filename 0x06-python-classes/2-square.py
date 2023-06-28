#!/usr/bin/python3
class Square:
    """A class with optional size initialisation, and type validation"""
    def __init__(self, size=0):
        """"Method to initialize the Square object"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
