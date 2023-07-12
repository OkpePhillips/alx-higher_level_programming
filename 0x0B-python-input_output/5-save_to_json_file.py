#!/usr/bin/python3
'''Module contains a function to serializean object to a file'''


import json
def save_to_json_file(my_obj, filename):
    '''Function to serialize an object to a file '''
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
        
