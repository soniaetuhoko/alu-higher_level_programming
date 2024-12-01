#!/usr/bin/python3
"""
This script lists all states with a name that matches the argument from the
database hbtn_0e_0_usa.
It takes four arguments: mysql username, mysql password, database name, and
state name searched.
The script is safe from MySQL injections.
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

    # Execute the SQL query to select states where name matches the argument
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Print each row (each state in the database matching the argument)
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
