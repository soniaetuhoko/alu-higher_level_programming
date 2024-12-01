#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
It takes three arguments: mysql username, mysql password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server running on localhost
    # at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects that contain the letter 'a'
    states_to_delete = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
    )

    # Delete each state in the list
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to apply the changes to the database
    session.commit()

    # Close the session
    session.close()
