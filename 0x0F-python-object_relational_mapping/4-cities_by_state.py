#!/usr/bin/python3
'''
Script to select all cities in the cities table
and order them by id in ascending order.
'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
