#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as
a parameter and displays the decoded body of the response."""

import urllib.request
import urllib.parse
import sys

    url_ = sys.argv[1]
    email_ = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email_)
    email = email.encode('ascii')
    url_req = urllib.request.Request(url_, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
