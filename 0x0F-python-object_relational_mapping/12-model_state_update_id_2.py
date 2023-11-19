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
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the State object with id = 2 exists
    if state_to_update:
        # Change the name of the State to "New Mexico"
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()
