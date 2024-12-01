#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument from
the database hbtn_0e_6_usa.
It takes four arguments: mysql username, mysql password, database name, and
state name to search.
The script is safe from MySQL injections.
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

    # Query the State object with the name passed as an argument
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
