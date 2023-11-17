#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Column, String
"""
Define database models class the class fort
the database
"""
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
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
