#!/usr/bin/python3
""" Module for square class with init method """


class Square:
    """A square of a certain size. Size is private to
        each instance of Square"""
    def __init__(self, size):
        """Method to initialize an object of Square"""
        self.__size = size
