#!/bin/bash
# Check if a URL is provided

if [ -z "$1" ]; then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Send a request to the URL using curl and store the response in a temporary file
temp_file=$(mktemp)
curl -s "$1" -o "$temp_file"

# Display the size of the response body in bytes
size=$(wc -c < "$temp_file")
echo "$size"

# Clean up the temporary file
rm "$temp_file"
