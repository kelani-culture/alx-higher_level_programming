#!/usr/bin/python3

"""
    LockedClass
"""


class LockedClass:
    """
        Locked Class
    """
    __slot__ = ("first_name",)

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'{__class__.__name__}' object has no attribute {name}")
