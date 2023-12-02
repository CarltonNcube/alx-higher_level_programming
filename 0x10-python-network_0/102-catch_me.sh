#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -L 0.0.0.0:5000/catch_me -d "You got me!"
