#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
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

    # Execute the SQL query to select all cities. Sort them by city ID
    # in ascending order.
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Print each row (city)
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
