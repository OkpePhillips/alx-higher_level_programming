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
    stateName = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities JOIN states ON\
                   cities.state_id = states.id WHERE\
                   states.name=%s ORDER BY cities.id ASC", (stateName,))
    cities = cursor.fetchall()

    city_names = ', '.join(city[0] for city in cities)
    print(city_names)

    cursor.close()
    db.close()
