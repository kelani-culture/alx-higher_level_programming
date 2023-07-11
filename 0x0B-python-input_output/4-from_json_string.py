#!/usr/bin/python3
""" json object to python """
json = __import__('json')


def from_json_string(my_str):
    """ json obejct to python """
    return json.loads(my_str)
