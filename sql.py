#No longer needed only kept around if I break somthing
import sqlite3

with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute('CREATE TABLE posts(title TEXT, details TEXT)')
	c.execute('INSERT INTO posts VALUES("This database", "is working.")')
	c.execute('INSERT INTO posts VALUES("This database", "is awesome.")')