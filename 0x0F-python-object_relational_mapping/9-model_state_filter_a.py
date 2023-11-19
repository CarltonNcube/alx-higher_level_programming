#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
        sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects containing the letter 'a' and sorted by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results as specified
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
