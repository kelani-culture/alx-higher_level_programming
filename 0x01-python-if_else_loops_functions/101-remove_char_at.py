#!/usr/bin/python3

def remove_char_at(str, n):
    len_str = len(str)

    if (n < 0):
        return (str)
    if (n > len_str):
        return (str)

    for i in str:
        if (i == str[n]):
            str = str[:n] + [n + 1:]
            break
    return (str)
