#!/usr/bin/python3
"""
Define the State class and Base for database model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declare the Base using declarative_base()
Base = declarative_base()

# Define the State class, inheriting from Base
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # If this script is executed directly, create the table in the database
    from sqlalchemy import create_engine

    # Create a SQLAlchemy engine to connect to the MySQL server
    # Use command-line arguments for MySQL username, password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
        sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the MySQL database based on the defined State class
    Base.metadata.create_all(engine)

