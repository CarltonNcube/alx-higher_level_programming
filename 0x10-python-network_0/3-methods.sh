#!/bin/bash
# Script to display all HTTP methods accepted by the server for a given URL using curl
curl -sI -X OPTIONS "$1" | awk -F ': ' '/Allow/ {gsub(",","",$2); print $2}'
