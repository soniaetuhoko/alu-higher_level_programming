#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q. If no argument is given, set q="".
If response body is properly JSON formatted and not empty, display id and name
Otherwise:
    - Display "Not a valid JSON" if the JSON is invalid
    - Display "No result" if the JSON is empty

Usage:
    ./8-json_api.py <letter>
"""

import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                                   json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
