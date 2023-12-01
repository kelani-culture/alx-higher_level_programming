#!/usr/bin/python3
import urllib.request
# a script that fetches https://alx-intranet.hbtn.io/status
url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(url) as response:
    body = response.read()
    content = body.decode('UTF-8')
    print(f"Body response:\n\t- type: {type(body)}")
    print(f"\t- content: {body}\n\t- utf8 content: {content}")
