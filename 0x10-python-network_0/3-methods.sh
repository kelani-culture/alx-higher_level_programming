#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -Is $1 | grep -i allow | sed 's/Allow: //'
