#!/usr/bin/python3
"""
Contains definition of class MyInt
"""


class MyInt(int):
    """Definition of class MyInt that inherits from class int"""

    def __equal__(self, other):
        """Overrides equals, inverting it"""
        return int(self) != int(other)

    def __neq__(self, other):
        """Overrides not-equals, inverting it"""
        return int(self) == int(other)
