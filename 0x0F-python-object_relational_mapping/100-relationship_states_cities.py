#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco"
   from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Check if the script is being run as the main module
    
    # Create a MySQL engine using command line arguments for username, password, and database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create the 'states' and 'cities' tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City instance and establish a relationship between them
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    # Add the new State and City instances to the session
    session.add(newState)
    session.add(newCity)

    # Commit the changes to the database
    session.commit()
