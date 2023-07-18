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
            return "[]"

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

    @staticmethod
    def obj_to_tuple(class_name, list_obj):
        """
            tuple
        """
        if class_name == "Square":
            return (list_obj.size, list_obj.x, list_obj.y, list_obj.id)
        else:
            return (list_obj.width, list_obj.height,
                    list_obj.x, list_obj.y, list_obj.id)

    @classmethod
    def save_to_file_csv(cls, list_obj):
        """
            save file to csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            for val in list_obj:
                row = Base.obj_to_tuple(cls.__name__, val)
                csv_writer.writerow(row)

    @classmethod
    def from_csv(cls, objs):
        """
            from csv file
        """
        class_name = cls.__name__
        # instantiate Square class
        if class_name == "Square" and len(objs) == 1:
            size = int(objs[0])
            return cls(size)
        elif class_name == "Square" and len(objs) == 2:
            size, x = int(objs[0]), int(objs[1])
            return cls(size, x)
        elif class_name == "Square" and len(objs) == 3:
            size, x, y = int(objs[0]), int(objs[1]), int(objs[2])
            return cls(size, x, y)
        elif class_name == "Square" and len(objs) == 3:
            size, x, y = int(objs[0]), int(objs[1]), int(objs[2])
            id = int(objs[3])
            return cls(size, x, y, id)

        else:
            if len(objs) == 2:
                width, height = int(objs[0]), int(objs[1])
                return cls(width, height)
            elif len(objs) == 3:
                width, height, x = int(objs[0]), int(objs[1]), int(objs[2])
                return cls(width, height, x)
            elif len(objs) == 4:
                width, height, x = int(objs[0]), int(objs[1]), int(objs[2])
                y = int(objs[3])
                return cls(width, height, x, y)
            elif len(objs) == 5:
                width, height, x = int(objs[0]), int(objs[1]), int(objs[2])
                y, id = int(objs[3]), int(objs[4])
                return cls(width, height, x, y, id)

    @classmethod
    def load_from_file_csv(cls):
        """
            Load file from csv
        """
        filename = cls. __name__+".csv"
        list_obj = []
        try:
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    obj = cls.from_csv(row)
                    list_obj.append(obj)
            return list_obj
        except FileNotFoundError:
            return list_obj
