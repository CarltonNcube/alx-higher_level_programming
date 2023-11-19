#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create a connection to the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print the results
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id).first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))
