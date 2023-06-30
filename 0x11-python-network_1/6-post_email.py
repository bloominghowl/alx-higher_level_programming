#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter and displays the body of the response.
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print(response.text)