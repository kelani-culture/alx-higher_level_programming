#!/usr/bin/python3
"""
 A python that contains the class definition
 of a state
"""

from sys import argv
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if len(argv) != 4:
    print("user password and database missing")
    exit(1)

try:
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".\
                           format(argv[1], argv[2], argv[3]))
except Exception as e:
    print(e)
    exit(1)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class State(Base):
    """
        A model for the state table
    """
    __tablename__ = "states"
    id = Column(Integer,primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    sesssion.commit()
    session.close()
