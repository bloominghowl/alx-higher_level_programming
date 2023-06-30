#!/usr/bin/python3
"""
Sends a request to a given URL, displays the body of the response,
and handles HTTP status codes greater than or equal to 400.
"""

import requests
import sys

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
