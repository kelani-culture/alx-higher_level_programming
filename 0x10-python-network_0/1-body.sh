#!/bin/bash
# display a 200 status
curl -s -L "$1" -o /dev/null -w '%{http_code}'; echo ""
