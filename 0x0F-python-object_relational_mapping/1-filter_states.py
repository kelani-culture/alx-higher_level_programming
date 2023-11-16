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
                 SELECT *
                 FROM states
                 WHERE name LIKE 'N%'
                 ORDER BY id;
                 """)

    for states in cur.fetchall():
        print(states)


arg = sys.argv

if len(arg) != 4:
    print("please provide complete credential dbusername password database")
    sys.exit()

connect_db(arg)
