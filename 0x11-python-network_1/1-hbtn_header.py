#!/usr/bin/python3
"""
script that takes in a URL, sends a request
to the URL and displays the value
"""
import urllib.request
import sys

if __name__ == "__main__":
    arg = sys.argv
    url = urllib.request.Request(arg[1])
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
