#!/usr/bin/python3
import MySQLdb
import sys

details = sys.argv

if (details) and (len(details) == 4):
    conn = MySQLdb.connect(host="localhost", port=3306, user=details[1],\
            passwd=details[2], db=details[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states") 
    state_list = cur.fetchall()
    for state in state_list:
        print(state)
