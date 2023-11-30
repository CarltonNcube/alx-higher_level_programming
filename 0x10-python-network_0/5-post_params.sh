#!/bin/bash
# Script to send a POST request with variables and display the body using curl
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
