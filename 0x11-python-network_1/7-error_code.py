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

    try:
        response = requests.get(endpoints)
        print(response.text)
    except HTTPError as e:
        print("Error code:", response.status_code)
