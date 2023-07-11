#!/usr/bin/python3

""" Append to a file """


def append_write(filename="", text=""):
    """
        Function that append to a file

        filename - name of file
        text - text to append file into
        Return: number of charactes to file
    """
    with open(filename, 'a') as f_append:
        f_app = f_append.write(text)
    return f_app
