#!/bin/bash
# Script to send a GET request and display the body for a 200 status code using curl
curl -sX GET $1 -L
