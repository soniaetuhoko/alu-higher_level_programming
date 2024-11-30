#!/usr/bin/python3
"""
This script sends a request to a URL and displays the value of the X-Request-Id
found in the header of the response.

It uses the urllib and sys packages.
"""

import urllib.request
import sys


def fetch_request_id(url):
    """Fetch the X-Request-Id header from the URL response and display it."""
    with urllib.request.urlopen(url) as response:
        # Get the X-Request-Id header
        request_id = response.getheader('X-Request-Id')
        print(request_id)

if __name__ == "__main__":
    # Take URL from the command line argument
    url = sys.argv[1]
    fetch_request_id(url)
