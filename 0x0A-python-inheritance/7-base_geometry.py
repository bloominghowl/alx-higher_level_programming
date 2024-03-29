#!/usr/bin/python3
"""This is a module container of the function 6-base_geometry.py
"""


class BaseGeometry:
    """A class with public instance method area and integer_validator"""
    def area(self):
        """raises an exception with a message when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
