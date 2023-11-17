#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


arg = sys.argv
if len(arg) != 4:
    print('please provide correct credential to connect to\
          database')
    sys.exit()

username, password, db_name = arg[1:4]

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        delete_state = session.query(State).filter(State.name.contains('a')).\
            all()
        for state in delete_state:
            session.delete(state)
            session.commit()
