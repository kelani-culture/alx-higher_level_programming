#!/usr/bin/python3
"""
    write to a file
"""


def write_file(filename="", text=""):
    """
        write to a file name
    """
    with open(filename, 'w') as f_write:
        fw = f_write.write(text)
        return fw
