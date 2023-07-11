#!/usr/bin/python3

"""
    read a file
"""


def read_file(filename=""):
    """
        function for reading file
    """
    with open(filename) as fd:
        read_fd = fd.read()
        print(read_fd)
