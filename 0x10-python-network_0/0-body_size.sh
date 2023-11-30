#!/bin/bash
# Script to display the size of the body in bytes for a given URL using curl
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
