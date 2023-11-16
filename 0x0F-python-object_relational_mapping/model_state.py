from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String
"""
Define database models class
"""
Base = declarative_base()


class State(Base):
    """
    state class model
    """
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)