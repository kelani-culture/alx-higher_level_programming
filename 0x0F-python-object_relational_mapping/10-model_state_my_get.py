#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


arg = sys.argv

if len(arg) != 5:
    print('provide complete informat to connect to db')
    sys.exit()

username, password, db_name, name = arg[1:5]
if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True)
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        get_state = session.query(State).filter(State.name == name).\
            first()

        if get_state:
            print(get_state.id)
        else:
            print('Not Found')
