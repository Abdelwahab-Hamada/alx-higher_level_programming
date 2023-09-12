#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """Append text in file"""

    with open(filename, 'a+') as f:
        return f.write(text)
