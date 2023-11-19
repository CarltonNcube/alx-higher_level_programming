#!/usr/bin/python3
"""
Start link class to table in database 
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declare the Base using declarative_base()
Base = declarative_base()

# Define the State class, inheriting from Base
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL server
    # Use command-line arguments for MySQL username, password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
        sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the MySQL database based on the defined State class
    Base.metadata.create_all(engine)

    # Optionally, create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
