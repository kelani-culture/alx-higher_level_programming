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

    try:
        response = requests.post(endpoint, params=params)
        response.raise_for_status()

        result = response.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
            print(f"Not a valid json")
