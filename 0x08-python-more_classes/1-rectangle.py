#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle props"""
    def __init__(self, width=0, height=0):
        """Recatangle Initiatilize"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
