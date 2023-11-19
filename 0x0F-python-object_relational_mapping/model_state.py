#!/usr/bin/python3
"""
Start link class to table in the database
"""

import sys
# Importing the Base and State classes from the model_state module
from model_state import Base, State

# Importing the create_engine function from the SQLAlchemy module
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Print debug information
    print("Command-line arguments:", sys.argv)

    # Creating a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
        sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Print debug information
    print("SQLAlchemy Engine URL:", engine.url)

    # Create the table in the MySQL database based on the defined State class
    Base.metadata.create_all(engine)
