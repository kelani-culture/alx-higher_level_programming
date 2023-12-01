#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests

endpoints = "https://alx-intranet.hbtn.io/stat"
request = requests.get('https://alx-intranet.hbtn.io/stat')
print(request)
