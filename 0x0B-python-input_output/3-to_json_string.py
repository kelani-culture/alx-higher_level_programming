#!/usr/bin/python3
""" working with json file """
json = __import__('json')


def to_json_string(my_obj):
    """ convert to json string """
    return json.dumps(my_obj)
