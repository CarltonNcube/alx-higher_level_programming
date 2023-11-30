#!/bin/bash
# Script to display all HTTP methods accepted by the server for a given URL using curl
curl -s -I -X OPTIONS "$1" | awk '/Allow/ {print $2}'
