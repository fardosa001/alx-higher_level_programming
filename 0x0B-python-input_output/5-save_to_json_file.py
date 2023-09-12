#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
