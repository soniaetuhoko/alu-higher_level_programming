#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code.

Usage:
    ./3-error_code.py <URL>
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
