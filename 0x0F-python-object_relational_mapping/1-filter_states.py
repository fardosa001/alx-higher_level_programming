#!/usr/bin/python3
"""lists all states that start with N"""
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
