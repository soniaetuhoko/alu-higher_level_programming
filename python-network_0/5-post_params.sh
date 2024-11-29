#!/bin/bash
# Sends a POST request to the URL with specified variables and displays the response body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
