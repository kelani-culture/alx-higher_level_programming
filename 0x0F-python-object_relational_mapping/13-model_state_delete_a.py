#!/usr/bin/python3
"""
delete state name that contain the
letter a
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv

def delete(user, passwd, db):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(user, passwd, db))
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception:
        print("engine not created")
        exit(1)

    del_a = (session.query(State).filter(State.name.like("%a%")).
             delete(synchronize_session=False))
    session.commit()

if __name__ == "__main__":
    delete(argv[1], argv[2], argv[3])
