#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """Is inistance"""

    return isinstance(obj, a_class) and type(obj) != a_class
