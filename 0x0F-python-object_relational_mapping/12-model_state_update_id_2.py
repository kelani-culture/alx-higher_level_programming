#!/usr/bin/python3
"""
update a state by id
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State,Base
from sys import argv

def update_byID(user, passwd, db):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("Engine not created")
        exit(1)

    state_id = (session.query(State).filter(State.id == 2).scalar())
    if state_id:
        state_id.name = "New Mexico"
        session.commit()
    else:
        print("invalid id")

if __name__ == "__main__":
    update_byID(argv[1], argv[2], argv[3])
