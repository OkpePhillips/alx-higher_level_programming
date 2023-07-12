#!/usr/bin/python3
''' Module contains a function that creates an object from a json file '''


import json
def load_from_json_file(filename):
    ''' Function that creates an object from a json file '''
    with open(filename, "r", encoding='utf-8') as f:
        obj = json.load(f)
        return obj
