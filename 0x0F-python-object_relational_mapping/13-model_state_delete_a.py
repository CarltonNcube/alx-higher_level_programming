#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def delete_states_with_a(username, password, database_name):
    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',
            pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    with Session() as session:
        # Query and delete State objects with a name containing the letter 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes to the database
        session.commit()

if __name__ == "__main__":
    # Check if correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Call the function with command-line arguments
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
