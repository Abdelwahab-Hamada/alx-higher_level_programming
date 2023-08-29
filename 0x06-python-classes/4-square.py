#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square properties"""
    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """Get square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get square area"""
        return (self.__size ** 2)
