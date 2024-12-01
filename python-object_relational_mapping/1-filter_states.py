#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the database
hbtn_0e_0_usa.
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

    # Execute the SQL query to select all states with names starting with 'N'
    cursor.execute(
            "SELECT * FROM states "
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
    )

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Print each row (each state in the database with a name starting with 'N')
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
