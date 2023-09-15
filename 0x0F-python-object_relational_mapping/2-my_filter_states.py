#!/usr/bin/python3
"""
A script that takes in an argument and display all the
its value if matches
"""
import MySQLdb
import sys

# Get user input
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Establish a connection
conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                       passwd=mysql_password, db=database_name)
cur = conn.cursor()

# Define the query with a placeholder
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

# Execute the query with the provided value
cur.execute(query, (state_name,))

# Fetch and print the results
results = cur.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
