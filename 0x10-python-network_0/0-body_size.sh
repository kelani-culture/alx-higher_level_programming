#!/usr/bin/bash
# print the content length in bytes
hostname=$1
port=$2

curl -so /dev/null "$hostname":"$port" -w '%{size_header}'