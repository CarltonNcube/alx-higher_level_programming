#!/usr/bin/python3
""" 
lists all states from the database hbtn_0e_0_usa 
"""

# Import necessary modules
import MySQLdb
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to select all states with a specific name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Iterate through the rows and print each one
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cur.close()
    db.close()
