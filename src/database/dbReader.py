import sqlite3


# Creating a database file for our database
connection = sqlite3.connect("words.db")

# Reading database
rows = connection.execute("select * from words")
for row in rows:
    print(row)

# Cleaning up
connection.commit()
connection.close()
