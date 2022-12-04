#!/usr/bin/python3
"""
class definition of a City
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class Definition of a City

    Attributes:
        __tablename__ (str): name of the table
        id (int): city record id
        name (str): city record name
        state_id (int): city record state id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
