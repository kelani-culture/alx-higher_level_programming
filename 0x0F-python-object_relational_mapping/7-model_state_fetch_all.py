#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

"""
retrieve state entry from database
"""

if len(sys.argv) != 4:
    print('Usage: python script.py <username> <password> <db_name>')
    sys.exit()

username, password, db_name = sys.argv[1:4]

engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)  # Ensure tables are created

        with Session() as session:
            states = session.query(State).order_by(State.id).all()
            for state in states:
                print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"An error occurred: {e}")
