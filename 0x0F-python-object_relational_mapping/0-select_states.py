#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Read command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(user=mysql_user, passwd=mysql_password, db=database_name, port=3306, host='localhost')

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
