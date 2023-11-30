#!/bin/bash
# display a 200 status
curl -s -o /dev/null "$1" -w '%{http_code}' | awk 'END {print $1 == 200 ? $0: "route 2"}'
