#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id header variable.
"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    x_request_id = headers.get("X-Request-Id")

print(x_request_id)
