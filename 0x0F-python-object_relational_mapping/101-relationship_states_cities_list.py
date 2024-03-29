#!/usr/bin/python3
""" 
Prints the State object with the name passed as an argument from the database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    # Create a MySQL engine using command line arguments for username, password, and database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create the 'states' and 'cities' tables in the database
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects and their corresponding City objects, ordered by State ID
    for instance in session.query(State).order_by(State.id):
        # Print State information
        print(instance.id, instance.name, sep=": ")
        
        # Print associated City information
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
