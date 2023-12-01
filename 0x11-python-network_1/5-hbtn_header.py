#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the value of the variable 
"""
import requests
import sys

if __name__ == "__main__":
    arg = sys.argv[1]
    endpoints = arg
    req = requests.get(endpoints)
    header = req.headers
    print(header.get('X-Request-Id'))
