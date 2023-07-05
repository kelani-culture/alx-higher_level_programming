#!/usr/bin/python3

"""
    Program that indent a line
"""

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if ' ' in text:
        word = text.split()
        for wrd in word:
            end = '\n\n' if ('.' in wrd or '?' in wrd or  ':' in wrd) else ' '
            print(wrd, end=end)
    else:
        for t in text:
            end = '\n\n' if ('.' == t or '?' == t or ':' in t) else ''
            print(t, end=end)
