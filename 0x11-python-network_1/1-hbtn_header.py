#!/usr/bin/python3
import urllib.request
import sys
"""
 script that takes in a URL, sends a
 request to the URL and displays the value of the
 X-Request-Id variable found in the header of the response.
"""

arg = sys.argv
url = urllib.request.Request(arg[1])
with urllib.request.urlopen(url) as response:
    headers = response.headers
    print(headers.get('X-Request-Id'))