#!/bin/bash
# print the content length in bytes
url=$1

curl -so /dev/null "$url" -w '%{size_download}'