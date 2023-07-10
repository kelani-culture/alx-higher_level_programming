#!/usr/bin/python3

"""
    check for subclass
"""


def inherits_from(obj, a_class):
    """
        check for a sub class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
