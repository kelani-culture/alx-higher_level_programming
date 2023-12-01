#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    arg = sys.argv
    endpoints = arg[1]
    email = arg[2]

    req = requests.post(endpoints, {'email': email})
    print(req.text)
