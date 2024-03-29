#!/usr/bin/python3
import MySQLdb
import sys


def connect_db(db_credential):
    try:
        db = MySQLdb.connect(user=arg[1], password=arg[2], database=arg[3],
                             port=3306)
    except Exception:
        print("could not connect to database")
        sys.exit()

    cur = db.cursor()
    cur.execute("""
                 SELECT c.id, c.name, s.name
                 FROM cities as c
                 JOIN states as s ON s.id = state_id
                 ORDER BY c.id;
                 """)

    filtered_states = cur.fetchall()
    for states in filtered_states:
        print(states)


arg = sys.argv

if len(arg) != 4:
    print("please provide complete credential dbusername password database")
    sys.exit()

if __name__ == "__main__":
    connect_db(arg)
