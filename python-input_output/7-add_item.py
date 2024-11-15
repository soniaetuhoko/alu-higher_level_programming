#!/usr/bin/python3
"""
A script that adds all command line arguments to a Python list, and then
saves them to a file as a JSON representation.
"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data from file, or start with empty list if file doesn't exist
if path.exists(filename):
    data = load_from_json_file(filename)
else:
    data = []

# Add command line arguments to the list
data.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(data, filename)
