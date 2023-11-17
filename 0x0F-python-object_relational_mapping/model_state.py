#!/usr/bin/python3
"""
Define database models class the class fort
the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
Base = declarative_base()


class State(Base):
    """
    state class model
    id: id (int)
    name name  (str)
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
