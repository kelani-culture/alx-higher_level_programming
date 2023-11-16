#!/usr/bin/python3
from sqlalchemy import create_engine
import sys
from model_state import Base

"""Start link class to table in database 
"""

arg = sys.argv

if len(arg) != 4:
    print("please provide complete information\
           username, password, db_username")
    sys,exit()
    
username = arg[1]
password = arg[2]
db_name = arg[3]



if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"\
                       .format(username, password, db_name),pool_pre_ping=True)
    Base.metadata.create_all(engine)
