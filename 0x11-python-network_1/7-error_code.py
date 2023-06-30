#!/usr/bin/python3
"""Sends a request to a given URL, displays the body of
the response, and handles HTTP status codes greater than 
or equal to 400."""


import sys
import requests

 response = requests.get(sys.argv[1])
 if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
 else:
        print(response.text)
