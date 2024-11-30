#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id
in the response header.

Usage:
    ./5-hbtn_header.py <URL>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
