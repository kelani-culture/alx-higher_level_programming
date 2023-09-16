#!/usr/bin/python3
"""
    list all cities in the database
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    info = sys.argv

    db = MySQLdb.connect(host='localhost', port=3306, user=info[1],
                         passwd=info[2], db=info[3])

    cursor = db.cursor()
    cursor.execute(""" SELECT cities.id, cities.name, states.name
                       FROM cities JOIN states ON
                       states.id = state_id
                       ORDER BY cities.id
                    """)

    cities = cursor.fetchall()
    for row in cities:
        print(row)

    cursor.close()
    db.close()
