import sqlite3

#create database
with sqlite3.connect("blog.db") as connection:

	#create cursor object
	conn = connection.cursor()

	#create table
	conn.execute(""" CREATE TABLE posts(title TEXT, post TEXT)""")


	#insert dummy data into table
	conn.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	conn.execute('INSERT INTO posts VALUES("Well", "I\'m Well.")')
	conn.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	conn.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')