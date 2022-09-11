#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

db = MySQLdb.connect(host='localhost',port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
cursor.execute('SELECT * from states ORDER BY id ASC')
states = cursor.fetchall()
for state in states:
    print(state)
cursor.close()
db.close()