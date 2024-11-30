#!/usr/bin/python3
"""
This script takes GitHub credentials (username and password)
and uses the GitHub API to display your id.

You must use Basic Authentication with a personal access token
as password to access your information (only read:user
permission is needed).

Usage:
    ./10-my_github.py <username> <password>
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")
