#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests

endpoints = "https://alx-intranet.hbtn.io/status"
request = requests.get(endpoints)
print(f"Body response:\n\t- type: {type(request.text)}")
print(f"\t- content: {request.text}")
