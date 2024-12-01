#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create engine and connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects sorted by cities.id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
