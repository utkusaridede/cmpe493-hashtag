import sqlite3
import json

print "What do you want to do?"
print "[1] INSERT DATASETS TO DATABASE"
print "[2] CREATE DATABASE"

option = input(" ~ ")

conn = sqlite3.connect('tweets.db')

def insertToTexts(docId, body):

	c = conn.cursor()
	c.execute('insert into TEXTS values (?,?)', (docId, body))
	conn.commit()
	conn.close()

def insertToHashtags(docId, hasht):

	c = conn.cursor()
	c.execute('insert into HASHTAGS values (?,?)', (docId, hasht))
	conn.commit()
	conn.close()

if option == 2:

	conn.execute('''CREATE TABLE TEXTS
	       (ID INT PRIMARY KEY     NOT NULL,
	       BODY        CHAR(200));''')

	conn.execute('''CREATE TABLE HASHTAGS
	       (ID INT PRIMARY KEY     NOT NULL,
	       HASHTAG     CHAR(100));''')

	print "Table created successfully";

	conn.close()

if option == 1:

	print "Which dataset do you want to insert?"
	
	setNum = raw_input(" ~ ")
	s = 'dataset' + setNum + '.json'
	tweets_data_path = s
	
	#insertToTexts(123,'ahmet')
