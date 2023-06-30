#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id variable in the response header.
"""

if __name__ == '__main__':
    import sys
    import requests
    try:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
    except Exception:
        pass
