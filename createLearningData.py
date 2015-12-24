import json
import sqlite3
import string

f = open('deneme.txt', 'w')
conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute("SELECT * FROM TEXTS")
rows = c.fetchall()
tweetBodies = []

for row in rows:
	tweet = row[1].split()

	for i in range(0, len(tweet)):
		if "http" in tweet[i]:
			tweet[i] = "~"
		elif "#" in tweet[i]:
			tweet[i] = "~"
		elif "@" in tweet[i]:
			tweet[i] = "~"
		elif "www" in tweet[i]:
			tweet[i] = "~"
		elif ".com" in tweet[i]:
			tweet[i] = "~"
		# Changing one letter in words.
		tweet[i] = tweet[i].replace("?", "~")
		tweet[i] = tweet[i].replace(".", "~")
		tweet[i] = tweet[i].replace(",", "~")

	text = ""
	for i in range(0, len(tweet)):
		if tweet[i] == "~" and len(text) == 0:
			pass
		elif tweet[i] == "~" and len(text) > 0 :
			f.write(text)
			f.write("\n")
			text = ""
		elif "~" in tweet[i]:
			text = text + "~" + tweet[i].replace("~", "")
			# Burada da basmak lazim
		elif "~" not in tweet[i]:
			text = text + "~" + tweet[i]
	if len(text) > 0:
		f.write(text)
		f.write("\n")

f.close()
conn.close()