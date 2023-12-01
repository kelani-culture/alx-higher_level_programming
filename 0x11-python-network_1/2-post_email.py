#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

arg = sys.argv

if __name__ == "__main__":
    url = arg[1]
    email = arg[2]
    data = {"email": email}
    new_data = urllib.parse.urlencode(data)
    request = new_data.encode('ascii')
    req = urllib.request.Request(url, request)
    with urllib.request.urlopen(req) as response:
        print('url')
        body = response.read()