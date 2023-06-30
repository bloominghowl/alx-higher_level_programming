#!/usr/bin/python3
"""
Sends a request to a given URL, displays the body of the response (decoded in utf-8),
and handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import sys
import urllib.error

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
