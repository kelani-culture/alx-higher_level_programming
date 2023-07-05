#!/usr/bin/python3

"""
    Program that indent a line
"""

def text_indentation(text):

    """
        index text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    word = text.split()
    for wrd in word:
        end = '\n\n' if ('.' in wrd or '?' in wrd or  ':' in wrd) else ' '
        print(wrd, end=end)
