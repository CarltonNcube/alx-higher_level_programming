#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
        sys.argv[2], sys.argv[3]))

    # Create the table in the MySQL database based on the defined State class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Search for the State object with the given name
    state_name_to_search = sys.argv[4]
    instance = session.query(State).filter(State.name == state_name_to_search).all()

    try:
        # Print the id of the found State object
        print(instance[0].id)
    except IndexError:
        # If no state with the given name is found, print "Not found"
        print("Not found")

    # Close the session
    session.close()
