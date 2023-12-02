#!/bin/bash
# Script to send a GET request and display the body for a 200 status code using curl
curl -s -w "%{http_code}" "$1" -o /dev/null | { read code; [ "$code" -eq 200 ] && curl -s "$1" || echo "Direct access"; }
