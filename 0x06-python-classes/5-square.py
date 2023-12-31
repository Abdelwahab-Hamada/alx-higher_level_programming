#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square properties"""
    def __init__(self, size):
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
        """Get square size"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
