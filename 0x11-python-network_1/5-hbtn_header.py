#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if 'X-Request-Id' in req.headers:
        print(req.headers['X-Request-Id'])
    else:
        pass
