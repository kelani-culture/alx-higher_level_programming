#!/usr/bin/python3
"""  function that returns the dictionary description """


def class_to_json(obj):
    """
        function that returns the dictionary description
        obj - instance of a class
    """
    return (obj.__dict__)
