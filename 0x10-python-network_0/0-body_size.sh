#!/bin/bash
# Check if the user has provided a URL

if [ -z "$1" ]
  then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Send a request to the URL using curl and store the response in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null $1)

# Display the size of the response body in bytes
echo "The size of the response body is $response bytes"
