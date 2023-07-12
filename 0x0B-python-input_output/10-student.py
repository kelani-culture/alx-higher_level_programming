#!/usr/bin/python3
"""
    A class student
"""


class Student:
    """
        A class that defines student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dict = {"first_name": self.first_name,
                        "last_name": self.last_name,
                        "age": self.age}
        if attrs:
            retrieved_student = {key: student_dict[key] for key in attrs
                                 if key in list(student_dict.keys())}
            return retrieved_student
        else:
            return student_dict
