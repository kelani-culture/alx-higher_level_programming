#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -d @"$2" -H "content-Type: application/json" -s "$1"
