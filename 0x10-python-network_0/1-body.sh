#!/bin/bash
# Script to send a GET request and display the body for a 200 status code using curl
curl -sL "$1" | [ "$(awk 'NR==1{print $2}')" -eq 200 ] && cat || echo "Error: Unexpected status code"
