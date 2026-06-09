#!/usr/bin/python3
"""Lists all states matching a given name from a MySQL database."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' ORDER BY id ASC".format(state_name)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
