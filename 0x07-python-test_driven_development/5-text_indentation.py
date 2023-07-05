#!/usr/bin/python3

"""
    Program that indent a line
"""


def text_indentation(text):

    """
        indent line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if ' ' in text:
        word = text.split()
        for ind, wrd in enumerate(word):
            if ind < len(word) - 1:
                end = '\n\n' if ('.' in word[ind] or '?' in word[ind] or
                                 ':' in word[ind]) else ' '
                print(word[ind], end=end)
            else:
                print(wrd, end="")
    else:
        for t in text:
            end = '\n\n' if ('.' == t or '?' == t or ':' in t) else ''
            print(t, end=end)
