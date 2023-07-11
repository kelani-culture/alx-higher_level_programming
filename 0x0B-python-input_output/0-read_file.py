#!/usr/bin/python3

"""
    read a file
"""


def read_file(filename=""):
    with open(filename) as fd:
        read_fd = fd.read()
        print(read_fd)
