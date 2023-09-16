#!/usr/bin/python3
"""
    write a safe SQL to prevent injection attack
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    info = sys.argv

    try:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=info[1], passwd=info[2], db=info[3])
    except Exception:
        print('failed to connect to database')
        sys.exit(1)

    curs = db.cursor()
    state_name = info[4]
    curs.execute("SELECT * FROM states WHERE name= %(name)s ORDER BY id",
                 {'name': state_name})

    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()
