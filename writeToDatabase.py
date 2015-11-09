import sqlite3

print "What do you want to do?"
print "[1] INSERT DATASETS TO DATABASE"
print "[2] CREATE DATABASE"

option = input(" ~ ")

if option == 2222:

	conn = sqlite3.connect('tweets.db')
	
	conn.execute('''CREATE TABLE TEXTS
	       (ID INT PRIMARY KEY     NOT NULL,
	       BODY        CHAR(200));''')

	conn.execute('''CREATE TABLE HASHTAGS
	       (ID INT PRIMARY KEY     NOT NULL,
	       HASHTAG     CHAR(100));''')

	print "Table created successfully";

	conn.close()

if option == 2:

	conn = sqlite3.connect('tweets.db')