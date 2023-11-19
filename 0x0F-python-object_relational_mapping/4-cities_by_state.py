#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # create cursor to exec queries using SQL, filter names starting with 'N'
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC"""

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()