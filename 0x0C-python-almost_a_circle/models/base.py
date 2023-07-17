#!/usr/bin/python3
import json

"""
   class base
"""


class Base:
    """
        Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        data = []
        if list_objs:
            data = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.json", "w") as fi:
            fi.write(cls.to_json_string(data))
