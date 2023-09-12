#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """Read file and print contnet"""

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
