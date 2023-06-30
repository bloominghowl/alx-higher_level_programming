#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of a repository
by a specific userusing the GitHub API."""

import requests
import sys

repository = sys.argv[1]
owner = sys.argv[2]

url = f"https://api.github.com/repos/{owner}/{repository}/commits"
response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]
    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
else:
    print("Error accessing GitHub API. Status Code:", response.status_code)
