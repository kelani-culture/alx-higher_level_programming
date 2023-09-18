#!/usr/bin/python3
"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def first_state(user, passwd, db):
    """
        a function that fetch the
        first state
    """
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("invalid value for user, passwd, db")
        exit(1)

    first_state = session.query(State).limit(1).all()

    if first_state:
        for state in first_state:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(argv) != 4:
        print("username password database missing")
        exit(1)
    first_state(argv[1], argv[2], argv[3])
