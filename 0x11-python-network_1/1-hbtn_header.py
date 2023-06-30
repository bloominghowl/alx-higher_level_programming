#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id header variable.
"""

if __name__ == '__main__':
    import urllib.request
    import sys
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    url_res = response.info()
    print(url_res['X-Request-Id'])
