#!/usr/bin/python3
""" load a json file """
json = __import__("json")


def load_from_json_file(filename):
    """ load json file """
    with open(filename) as f_json:
        load_json = json.load(f_json)

    return load_json
