#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Only execute this when run as a script
if __name__ == "__main__":
    import sys
    # Create an engine that connects to the MySQL server
    # running on localhost at port 3306.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)
