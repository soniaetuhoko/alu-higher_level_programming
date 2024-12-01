#!/usr/bin/python3
"""
Contains the class definition of a City and an instance of Base using
SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    City class:
    - Inherits from Base.
    - Links to the MySQL table `cities`.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
