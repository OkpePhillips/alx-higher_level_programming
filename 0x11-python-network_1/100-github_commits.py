#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repository)
    req = get(url)
    json_object = req.json()
    if json_object:
        for i in range(0, 10):
            print("{}: {}".format(json_object[i].get('sha'),
                                  json_object[i].get('commit')
                                  .get('author').get('name')))
