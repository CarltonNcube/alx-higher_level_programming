#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and display the response body
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
