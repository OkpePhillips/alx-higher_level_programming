#!/usr/bin/python3
'''
Script to list states from a database where condition is
passed as argument. it is safe from SQL injection.
'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY\
                   states.id ASC".format(state_name))
    states = cursor.fetchall()

    for id, state in states:
        print("({}, '{}')".format(id, state))

    cursor.close()
    db.close()
