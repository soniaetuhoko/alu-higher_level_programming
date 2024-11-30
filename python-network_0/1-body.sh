#!/bin/bash
# Bash script to send a GET request and display the body of the response if the status code is 200
curl -sL -w "%{http_code}" "$1" -o /tmp/response_body | grep -q "200" && cat /tmp/response_body
