#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
from urllib import parse, request
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    reqs = request.Request(sys.argv[1], data)
    with request.urlopen(reqs) as response:
        page = response.read()
        print(page.decode('utf-8'))
