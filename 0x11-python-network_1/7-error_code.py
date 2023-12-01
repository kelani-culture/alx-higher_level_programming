#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    arg = sys.argv
    endpoints = arg[1]

    response = requests.get(endpoints)
    if int(response.status_code) >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
