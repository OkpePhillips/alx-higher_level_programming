#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
