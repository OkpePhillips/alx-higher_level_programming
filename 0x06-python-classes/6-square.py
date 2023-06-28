#!/usr/bin/python3
class Square:
    """A class with getter and setter, as well as value and type validation
        for the size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize a square object"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("postion must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to calculate area of a square object"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print a square object in specified size"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)
