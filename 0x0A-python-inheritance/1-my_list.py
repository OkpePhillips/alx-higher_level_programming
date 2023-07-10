#!/usr/bin/python3
''' Module contains a class with inheritance'''


class MyList(list):
    ''' Class that inherits the attributes of list super class '''

    def print_sorted(self):
        ''' Prints the elements of list in ascending order'''
        my_list = self.copy()
        my_list.sort()
        print(my_list)

