#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Safe from SQL injection.
"""

import MySQLdb
import sys

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306)
cur = db.cursor()

# Use parameterized query to prevent SQL injection
query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
result = cur.execute(query, (sys.argv[4],))

# Check if the query was successful
if result > 0:
    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print each row (state) in the result set
    for row in rows:
        print(row)
else:
    # Handle the case where the query was not successful
    print("Error executing the query")

# Close the cursor and database connection
cur.close()
db.close()
