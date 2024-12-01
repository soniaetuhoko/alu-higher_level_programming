#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes four arguments: mysql username, mysql password, database name, and
state name.
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

    # Prepare the SQL query to be safe from SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with parameter substitution to prevent SQL injection
    cursor.execute(query, (sys.argv[4],))

    # Fetch all the results of the query
    rows = cursor.fetchall()

    # Print the results as comma-separated city names
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
