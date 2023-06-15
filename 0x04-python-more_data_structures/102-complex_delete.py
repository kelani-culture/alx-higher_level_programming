#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is None:
        return None
    dict_keys = [keys for keys, val in a_dictionary.items() if value == val]

    for key in dict_keys:
        del a_dictionary[key]
    return a_dictionary
