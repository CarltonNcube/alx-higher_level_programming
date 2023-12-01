#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id variable"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Check if 'X-Request-Id' is present in the headers
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
