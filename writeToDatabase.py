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

def insertToHashtags(docId, hasht):

	c = conn.cursor()
	c.execute('insert into HASHTAGS values (?,?)', (docId, hasht))
	conn.commit()

if option == 2:

	conn.execute('''CREATE TABLE TEXTS
	       (ID INT PRIMARY KEY     NOT NULL,
	       BODY        CHAR(200));''')

	conn.execute('''CREATE TABLE HASHTAGS
	       (ID INT     NOT NULL,
	       HASHTAG     CHAR(100));''')

	print "Table created successfully";

	conn.close()

if option == 1:

	print "Which dataset do you want to insert?"
	
	setNum = raw_input(" ~ ")
	s = 'dataset' + setNum + '.json'
	tweets_data_path = s

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	
	for line in tweets_file:
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue

	for tw in tweets_data:
		tw_text = tw['text']
		tw_text = tw_text.replace('\n', ' ')
		tw_text = tw_text + ' '
		tw_id = tw['id']

		insertToTexts(tw_id,tw_text)

		hash_index = [pos for pos, char in enumerate(tw_text) if char == '#']
		space_index = [pos for pos, char in enumerate(tw_text) if char == ' ']

		spaceCounter = 0
		for i in range(0,len(hash_index)):
			for k in range(0,len(space_index)):

				if i < len(hash_index)-1:
					if hash_index[i+1] > space_index[spaceCounter] and hash_index[i] > space_index[spaceCounter]:
						spaceCounter += 1
					elif hash_index[i+1] > space_index[spaceCounter] and hash_index[i] < space_index[spaceCounter]:
						hashtag = tw_text[hash_index[i]+1:space_index[spaceCounter]]
						if len(hashtag) != 0:
							insertToHashtags(tw_id,hashtag)
						break
					else:
						hashtag = tw_text[hash_index[i]+1:hash_index[i+1]]
						if len(hashtag) != 0:
							insertToHashtags(tw_id,hashtag)
						break
				else:
					if hash_index[i] > space_index[spaceCounter]:
						spaceCounter += 1
					else:
						hashtag = tw_text[hash_index[i]+1:space_index[spaceCounter]]
						if len(hashtag) != 0:
							insertToHashtags(tw_id,hashtag)
						break
conn.close()