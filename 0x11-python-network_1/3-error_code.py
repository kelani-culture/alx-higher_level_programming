#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    arg = sys.argv[1]
    req = Request(arg)
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode('UTF-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
