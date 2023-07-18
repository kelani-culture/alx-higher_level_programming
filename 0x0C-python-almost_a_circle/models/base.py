#!/usr/bin/python3
"""
   A program that define a base class
   for each child to inherits
"""
import json
import csv


class Base:
    """ The base class for other classes.
        This class serves as a parent class that provides common
        functionality and attribute for its derived classes.
        Attributes:
            id (int): The identity of the instance.

        Methods:
            __init__: Initialize a new instance of the Base class.
            save_to_file: save to a json file
            to_json_string: convert python object to a json string
            from_json_string: convert json object to python object
            create: create a dummy instance for each class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
           initializes a new base

           Parameter:
                    id - default None
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # write a list of dictionaryies as json string
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Write a list of dictionary to json string
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps("[]")

    # write to a json string
    @classmethod
    def save_to_file(cls, list_objs):
        """
            save to a jsin file
        """
        data = []
        if list_objs:
            data = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.json", "w") as fi:
            fi.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """
            loads a json string to python object
        """
        if json_string and len(json_string) > 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
           create a dummy instance
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
            dummy_instance.update(**dictionary)
        else:
            dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
            Load a file that exists
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename) as fi:
                list_dict = Base.from_json_string(fi.read())
                return [cls.create(**di) for di in list_dict]
        except FileNotFoundError:
            return []

    # write to a csv file
    def save_to_file_csv(cls, list_objs):
        """
            Write a file to a csv file
        """
        filename = f"{cls.__name__}.csv"

        with open(filename, 'w') as csv_file:
            csv_w = csv.writer(Base.to_json_string(list_objs))
            return csv_w
