#!/usr/bin/python3
'''Module contains a function that returns JSON of an object '''


import json
def to_json_string(my_obj):
    '''Function to create the JSON representation of an object '''
    json_format = json.dumps(my_obj)
    return json_format
