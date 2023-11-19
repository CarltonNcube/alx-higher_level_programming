#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all cities and order them by ID
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print each row (city) in the result set
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
