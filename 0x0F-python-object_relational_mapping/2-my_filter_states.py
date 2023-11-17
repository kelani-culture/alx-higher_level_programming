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
                 WHERE name = '{}'
                 ORDER BY id;
                 """.format(arg[4]))

    for states in cur.fetchall():
        print(states)


arg = sys.argv


if __name__ == "__main__":
    connect_db(arg)
