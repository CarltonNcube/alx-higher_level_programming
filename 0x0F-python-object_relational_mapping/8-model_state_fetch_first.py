#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL server
    # Use command-line arguments for MySQL username, password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the table in the MySQL database based on the defined State class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object from the database
    instance = session.query(State).first()

    # Check if the instance is None and print the result accordingly
    if instance is None:
        print("Nothing")
    else:
        # Print the id and name of the first State object
        print(instance.id, instance.name, sep=": ")
