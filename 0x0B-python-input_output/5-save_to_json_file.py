#!/usr/bin/python3
"""5-save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """Write JSON to file"""

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
