#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
