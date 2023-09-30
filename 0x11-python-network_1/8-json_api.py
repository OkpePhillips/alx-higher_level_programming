#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    data['q'] = sys.argv[1]

    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_object = req.json()
        if not json_object:
            print("No result")
        else:
            print("[{}] {}".format(json_object.get('id'), json_object.get('name')))
    except:
        print("Not a valid JSON")
