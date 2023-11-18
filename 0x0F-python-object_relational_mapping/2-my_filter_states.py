#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        exit(1)

    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the SQL query to select states with a specific name (case-sensitive) and order them by ID
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY id ASC".format(sys.argv[4]))

    # Fetch all rows from the result set
    query_rows = cur.fetchall()

    # Print each row (state) in the result set
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
