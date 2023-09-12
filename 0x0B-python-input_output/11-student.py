#!/usr/bin/python3
"""11-student"""


class Student:
    """Student props"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary Student"""

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attrs of student"""

        for x in json:
            self.__dict__.update({x: json[x]})
