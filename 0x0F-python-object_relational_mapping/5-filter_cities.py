#!/usr/bin/python3
"""
a select query that list cities by states
"""
import MySQLdb
import sys

if __name__ == '__main__':
    
    try:
        info = sys.argv

        if len(info) - 1 < 4:
            print("username, passwd, database not provided")
            exit(1)
        db = MySQLdb.connect(host='localhost', port=3306, user=info[1],
                             passwd=info[2], db=info[3])
    except Exception:
        print("failed to connect to database")
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute("""
                     SELECT cities.name
                     FROM cities
                     JOIN states ON states.id = state_id
                     WHERE states.name = %(name)s
                     ORDER BY cities.id
                    """, {'name': info[4]})
    cities = cursor.fetchall()
    city = ', '.join(i for item in cities for i in item)
    print(city)

    cursor.close()
    db.close()
