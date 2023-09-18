#!/usr/bin/python3
"""
    add a new state to the database
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def add_state(user, passwd, db):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("engine not created")
        exit(1)

    state = State(name="Louisiana")
    session.add(state)
    session.commit()


if __name__ == "__main__":
    add_state(argv[1], argv[2], argv[3])
