#!/usr/bin/python3
""" write to a json file """
json = __import__('json')


def save_to_json_file(my_obj, filename):
    """ write to a json file """
    with open(filename, 'w') as f_json:
        f_write = json.dump(my_obj, f_json)
