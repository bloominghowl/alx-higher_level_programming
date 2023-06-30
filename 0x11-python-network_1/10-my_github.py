#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to display the user id.
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = "https://api.github.com/user"
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    json_data = response.json()
    user_id = json_data.get("id")
    print("User ID:", user_id)
else:
    print("Error accessing GitHub API. Status Code:", response.status_code)
