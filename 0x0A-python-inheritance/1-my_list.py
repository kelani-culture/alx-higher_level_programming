#!/usr/bin/python3

"""
    append to list
"""


class MyList(list):
    """
        print sorted list
    """
    def print_sorted(self):
        nl = self[:]
        nl.sort()
        print(nl)
