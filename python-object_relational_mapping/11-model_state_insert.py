#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()
