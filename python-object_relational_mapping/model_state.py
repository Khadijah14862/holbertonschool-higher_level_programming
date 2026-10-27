#!/usr/bin/python3
"""Define the State model using SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represent a state in the MySQL states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
