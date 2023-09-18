#!/usr/bin/python3
"""
fetch all states in the database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv


def list_states(username, passwd, db):
    try:
        engine = create_engine(f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}")

        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("invalid")
        exit(1)

    state_list = session.query(State).order_by(State.id).all()
    
    for state in state_list:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    if len(argv) != 4:
        print("missing database info field")
        exit(1)

    username, passwd, db = argv[1], argv[2], argv[3]
    list_states(username, passwd, db)
