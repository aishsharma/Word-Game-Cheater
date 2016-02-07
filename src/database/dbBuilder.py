import sqlite3

# Creating a database file for our database
connection = sqlite3.connect("words.db")

connection.execute('''
	Create table words (
			id integer primary key,
			word text not null,
			length int not null
		)
	''')

print("Database created successfully.")

# Opening the words file
with open("words.txt", "r") as f:
    for line in f:
        line = line.strip()  # Removing any trailing blank spaces
        if line.isalpha():  # Checking to see if word only has alphabets.
            print(line)
            connection.execute(
                "insert into words (word, length) values ('{0}', {1})".format(
                    line, len(line)))

print("words copied successfully into sqlite database")

# Cleaning up
connection.commit()
connection.close()
