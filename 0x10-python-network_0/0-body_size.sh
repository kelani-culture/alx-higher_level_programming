#!/bin/bash
# print the content length in bytes
curl -so /dev/null "$1" -w '%{size_download}'; echo ""
