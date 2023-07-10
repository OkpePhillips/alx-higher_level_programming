#!/usr/bin/python3
'''
    Module raises an exception for a public instance  method.

    Another instance method handles value validation.
'''


class BaseGeometry:
    """ Class with a public instance method """
    def area(self):
        '''
        An umimplemented method that raises exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        A method to validate value.

        Arguments:
            name: name of property
            value: the value of the property

        Exceptions:
            ValueError: If value is < 0
            TypeError: If value is not an integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
