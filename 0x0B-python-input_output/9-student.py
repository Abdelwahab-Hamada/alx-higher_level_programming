#!/usr/bin/python3
"""9-student"""


class Student:
    """Student props"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary of student class"""

        return self.__dict__
