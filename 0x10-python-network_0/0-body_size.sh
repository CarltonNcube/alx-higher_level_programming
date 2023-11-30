#!/bin/bash
# Script to retrieve the body size of a request using curl

curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
