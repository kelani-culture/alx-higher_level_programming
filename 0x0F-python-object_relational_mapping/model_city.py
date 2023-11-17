#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, ForeignKey
from model_state import Base

"""Create the model for city
    that contains the city attribute
"""



class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)