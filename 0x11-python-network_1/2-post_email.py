#!/usr/bin/python3
"""Sends a POST request to a URL with an email as a parameter"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')

    with request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("{}".format(body))
