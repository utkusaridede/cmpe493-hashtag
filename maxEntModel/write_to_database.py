#!/usr/bin/python
# -*- coding: utf8 -*-
import sqlite3
import json

print "What do you want to do?"
print "[1] INSERT DATASETS TO DATABASE"
print "[2] CREATE DATABASE"

option = input(" ~ ")

conn = sqlite3.connect('tweets.db')

def insertToTexts(docId, body):

	c = conn.cursor()
	c.execute('insert or ignore into TEXTS values (?,?)', (docId, body))

def insertToHashtags(docId, hasht):

	c = conn.cursor()
	c.execute('insert or ignore into HASHTAGS values (?,?)', (docId, hasht))

if option == 2:

	conn.execute('''CREATE TABLE TEXTS
	       (ID INT PRIMARY KEY     NOT NULL,
	       BODY        CHAR(200));''')

	conn.execute('''CREATE TABLE HASHTAGS
	       (ID INT     NOT NULL,
	       HASHTAG CHAR(100) UNIQUE);''')

	print "Table created successfully";

	conn.close()

if option == 1:

	print "Which dataset do you want to insert?"
	
	setNum = raw_input(" ~ ")
	s = './datasets/dataset' + setNum + '.json'
	tweets_data_path = s

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	i = 0
	for line in tweets_file:
		i += 1
		try:
			tweet = json.loads(line)

			if not 'limit' in tweet:
				tw_text = tweet['text']
				if not tw_text.startswith('RT'):
					tw_text = tw_text.replace('\n', ' ')
					tw_text = tw_text + ' '
					tw_id = tweet['id']

					insertToTexts(tw_id,tw_text)
					space_index = [pos for pos, char in enumerate(tw_text) if char == ' ']

					counter = 0
					for k in range(0,len(space_index)):

						string = tw_text[counter:space_index[k]]
						if string.startswith('#'):
							string = string[1:]

							if len(string) > 0 and not '#' in string:
								if string.startswith('_') and len(string) == 1:
									counter = space_index[k] + 1
								else:
									index = 0
									for s in string:
										if not s in u"_abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789":
											break
										else:
											index = index + 1
									hashtag = string[0:index]
									if len(hashtag) > 0:
										insertToHashtags(tw_id,hashtag)
									counter = space_index[k] + 1
							else:
								counter = space_index[k] + 1
						else:
							counter = space_index[k] + 1
		except:
			continue
		if i %1000==0:
			conn.commit()
conn.commit()			
conn.close()