#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io and displays the response information.
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode("utf-8"))
