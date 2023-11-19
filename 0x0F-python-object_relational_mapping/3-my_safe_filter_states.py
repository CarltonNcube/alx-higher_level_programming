#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Get the state name to match from command-line arguments
    match = sys.argv[4]

    # Use a parameterized query to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match,))

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print each row (state) in the result set
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
