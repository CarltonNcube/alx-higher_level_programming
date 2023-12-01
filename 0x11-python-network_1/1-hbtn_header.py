#!/usr/bin/python3
"""Takes in a URL, sends a request, and displays the value of the X-Request-Id header"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
