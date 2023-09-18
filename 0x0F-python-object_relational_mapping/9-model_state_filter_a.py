#!/usr/bin/python3
"""
 a script that lists all State objects that
 contain the letter a from the database
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def start_with_a(user, passwd, db):

    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("Invalid value")
        exit(1)

    states = (session.query(State).filter(State.name.like("%a%"))
              .order_by(State.id).all())
    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    if len(argv) != 4:
        print("user, password, database missing")
        exit(1)

    start_with_a(argv[1], argv[2], argv[3])
