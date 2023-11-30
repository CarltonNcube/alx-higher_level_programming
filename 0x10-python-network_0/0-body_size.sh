#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Construct the full URL with http:// prefix (if not provided)
url=$1
if [[ ! $url =~ ^http:// && ! $url =~ ^https:// ]]; then
    url="http://$url"
fi

# Send a request to the URL using curl and store the response in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body in bytes
echo "$response"
