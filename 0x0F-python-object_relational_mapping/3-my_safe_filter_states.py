#!/usr/bin/python3
"""This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!"""

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
    query = "SELECT * FROM states \
                    WHERE name=%s \
                    ORDER BY id ASC"
    cursor.execute(query, (argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
