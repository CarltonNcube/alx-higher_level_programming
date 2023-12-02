#!/bin/bash
# Usage: ./script.sh <URL> <filename>
[ "$#" -eq 2 ] && curl -s -X POST -H "Content-Type: application/json" --data "@$2" "$1"
