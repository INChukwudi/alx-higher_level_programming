#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    Represents a class definition of a State

    __tablename__ (str): name of the MySQL table
    id (sqlalchemy.Integer): state record id
    name (sqlalchemy.String): state record name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
