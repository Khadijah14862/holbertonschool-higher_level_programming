#!/usr/bin/python3
"""List all cities belonging to a given state."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = (
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (sys.argv[4],))

    cities = [city[0] for city in cursor.fetchall()]

    print(", ".join(cities))

    cursor.close()
    db.close()
