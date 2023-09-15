#!/usr/bin/python3
"""
    list all states that start with
    the letter N
"""
import MySQLdb
import sys

info = sys.argv

if info and len(info) == 4:
    conn = MySQLdb.connect(host="localhost", port=3306, user=info[1],
                           passwd=info[2], db=info[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id")
    state_list = cur.fetchall()
    for state in state_list:
        print(state)
