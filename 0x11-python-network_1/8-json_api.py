#!/usr/bin/python3
"""
a Python script that takes in a
letter and sends a POST request
"""
import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    params = {'q': q}
    endpoint = "http://0.0.0.0:5000/search_user"
    req = requests.get("http://0.0.0.0:5000/search_user", params=params)
    try:
        res = req.json()
        if not res:
            print("No result")
        else:
            print(f"[{res['id']}] {res['name']}")
    except Exception:
        print("Not a valid JSON")
