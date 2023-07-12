#!/usr/bin/python3
'''Module contains a function that returns python data from json '''


import json


def from_json_string(my_str):
    '''
    Function that returns python data structre from json format
    '''
    python_obj = json.loads(my_str)
    return python_obj
