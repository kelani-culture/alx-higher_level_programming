#!/usr/bin/python3
"""
A script that takes in an argument and display all the
its value if matches
"""
import sys
import MySQLdb

info = sys.argv

if info and len(info) == 5:
    conn = MySQLdb.connect(host="localhost", port=3306, user=info[1],
                           passwd=info[2], db=info[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (info[4],))
    row = cur.fetchall()
    for r in row:
        print(r)

    cur.close()
    conn.close()
