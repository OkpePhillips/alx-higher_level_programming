#!/usr/bin/python3
"""
Script that takes a url, sends a request to that url and
displays the value of `X-Request-Id` variable.
"""
import urllib.request
import sys


if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        page = response.info()
        print(page.get('X-Request-Id'))
