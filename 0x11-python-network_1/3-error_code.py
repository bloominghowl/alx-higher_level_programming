#!/usr/bin/python3
"""
Sends a request to a given URL, displays the body of the response (decoded in utf-8),
and handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys

url = urllib.request.Request(sys.argv[1])

try:
    with urllib.request.urlopen(url) as response:
         url_res = response.read()
         print(url_res.decode('utf-8'))

except urllib.error.HTTPError as err:
    print("Error code: {}",.format(err.code))
