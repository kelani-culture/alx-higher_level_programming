#!/usr/bin/python3
"""Create the model for city
    that contains the city attribute
"""
from sqlalchemy import Integer, Column, String, ForeignKey
from model_state import Base


class City(Base):
    """
    attribute of class city
    id: int
    name: string
    state_id: foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
