#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Send a request to the URL using curl and display the size of the response body in bytes
curl -Is "$1" | grep -i -w 'Content-Length' | awk '{print $2}' | tr -d '\r'
