#!/usr/bin/python3
"""
Takes in GitHub repo and owner name to list 10 commits (from the most recent to oldest).
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{}/{}/commits"
    response = requests.get(url)

    if response.status_code >= 400:
        print('None')
    else:
        for commit in response.json()[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
