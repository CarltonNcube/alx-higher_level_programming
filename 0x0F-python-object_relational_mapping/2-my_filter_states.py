#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Connect to the MySQL database
        with MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                db=sys.argv[3], port=3306) as db:
            # Create a cursor object to interact with the database
            with db.cursor() as cur:
                # Execute the SQL query with a parameterized query
                cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (sys.argv[4],))

                # Fetch all rows from the result set
                query_rows = cur.fetchall()

                # Print each row (state) in the result set
                for row in query_rows:
                    print(row)

    except MySQLdb.Error as e:
        print(f"Database Error: {e}")
        sys.exit(1)

