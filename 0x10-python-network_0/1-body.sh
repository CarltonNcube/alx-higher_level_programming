#!/bin/bash
# Script to send a GET request and display the body for a 200 status code using curl
curl -sI "$1" | grep "HTTP/1.1 200 OK" && curl -sL "$1" || echo "Error: Unexpected status code"
