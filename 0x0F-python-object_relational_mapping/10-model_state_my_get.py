#!/usr/bin/python3
"""
a script that prints the State object with the name
passed as argument from the database
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
import re


def state_id(user, passwd, db, state):
    try:
        engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("failed to create database engine")
        exit(1)
    pattern = re.match(r"^[a-zA-Z]+$", state)
    if pattern:
        state_obj = session.query(State.id).filter(State.name == state).scalar()
        if state_obj:
            print(state_obj)
        else:
            print("Not found")
    else:
        print("No match")


if __name__ == "__main__":
    if len(argv) != 5:
        print("username, password, database, states inputs missing")
        exit(1)
    state_id(argv[1], argv[2], argv[3], argv[4])
