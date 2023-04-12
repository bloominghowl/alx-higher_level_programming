#!/usr/bin/python3
"""
This is a module container of function 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    checking if the object is an instance of a specified class
        Args:
            obj: initial object
            a_class: class to confirm the object
            Returns: True if object is an instance of, or inherited the specified class
                     False if otherwise
    """
    return isinstance(obj, a_class)
