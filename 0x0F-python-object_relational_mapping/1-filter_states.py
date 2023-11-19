#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get database credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states with names starting with 'N'
    # (case-sensitive) and order them by ID
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print each row (state) in the result set
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

