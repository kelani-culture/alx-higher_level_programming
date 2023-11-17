#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
"""
print first stae in database
"""

arg = sys.argv

if len(arg) != 4:
    print("incomplete information to connect to database")
    sys.exit()

username, password, db_name = arg[1:4]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    try:
        with Session() as session:
            state = session.query(State).order_by(State.id).first()
            if state:
                print(f'{state.id}: {state.name}')
            else:
                print('Nothing')
    except Exception as e:
        print("Exception:", e)
