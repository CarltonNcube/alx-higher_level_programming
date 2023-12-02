#!/bin/bash
# Sends a request to a URL and displays only the status code using curl
curl -o /dev/null -sw "%{http_code}" "$1"
