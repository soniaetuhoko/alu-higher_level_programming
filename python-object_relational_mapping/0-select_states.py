#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes three arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to select all states ordered by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Print each row (each state in the database)
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
