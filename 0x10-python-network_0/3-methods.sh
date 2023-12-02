#!/bin/bash
# Script to display all HTTP methods accepted by the server for a given URL using curl
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
