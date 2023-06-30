#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter and displays the decoded body of the response.
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    body = response.read().decode('utf-8')

print(body)
