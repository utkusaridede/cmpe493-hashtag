import json
import sqlite3
import string

f = open('deneme.txt', 'w')
conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute("SELECT * FROM TEXTS")
rows = c.fetchall()
tweetBodies = []
ourChars = string.punctuation + "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def prepareFeatures(text):

	textSize = len(text)
	for i in range(0, textSize):
		if text[i] != "~":
			if text[i-1] == "~":
				f.write("B\t")
			else:
				f.write("I\t")
			# Feature 1
			f.write("m1=")
			for j in range(0,3):
				if i+j < textSize:
					if text[i+j] != "~":
						f.write(text[i+j].lower())
					else:
						if i+j+1 < textSize:
							f.write(text[i+j+1].lower())
						else:
							f.write("@")	
				else:
					f.write("@")
			f.write(" ")
			# Feature 2
			f.write("m2=")
			for j in range(0,3):
				if i+j < textSize:
					if text[i+j] != "~":
						f.write(text[i+j])
					else:
						if i+j+1 < textSize:
							f.write(text[i+j+1])
						else:
							f.write("@")
				else:
					f.write("@")
			f.write(" ")
			# Feature 3
			f.write("m3=")
			for j in range(0,3):
				if i+j < textSize and text[i+j] != "~":
					if text[i+j].islower():
						f.write("x")
					elif text[i+j].isupper():
						f.write("X")
				elif i+j < textSize and text[i+j] == "~":
					if i+j+1 < textSize:
						if text[i+j+1].islower():
							f.write("x")
						elif text[i+j+1].isupper():
							f.write("X")
					else:
						f.write("@")
				else:
					f.write("@")
			f.write(" ")
			# Feature 4
			f.write("m4=")
			if i-1 == 0:
				f.write("@")
			else:
				if text[i-1] == "~":
					if text[i-2].islower():
						f.write("x")
					elif text[i-2].isupper():
						f.write("X")
				else:
					if text[i-1].islower():
						f.write("x")
					elif text[i-1].isupper():
						f.write("X")
			if text[i].islower():
				f.write("x")
			elif text[i].isupper():
				f.write("X")
			if i+1 < textSize:
				if text[i+1] == "~":
					if i+2 < textSize:
						if text[i+2].islower():
							f.write("x")
						elif text[i+2].isupper():
							f.write("X")
					else:
						f.write("@")
				else:
					if text[i+1].islower():
						f.write("x")
					elif text[i+1].isupper():
						f.write("X")
			else:
				f.write("@")
			f.write("\n")


for row in rows:
	tweet = row[1].split()
	for i in range(0, len(tweet)):
		for letter in tweet[i]:
			if letter not in ourChars:
				tweet[i] = tweet[i].replace(letter, "~")
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
		for item in string.punctuation:
			tweet[i] = tweet[i].replace(item, "~")

	text = ""
	for i in range(0, len(tweet)):
		if tweet[i] == "~" and len(text) == 0:
			continue
		elif tweet[i] == "~" and len(text) > 0 :
			prepareFeatures(text)
			text = ""
		elif "~" in tweet[i]:
			text = text + "~" + tweet[i][:tweet[i].find("~")]
			if len(text) > 1:
				prepareFeatures(text)
			text = ""
		elif "~" not in tweet[i]:
			if len(tweet[i]) > 0:
				text = text + "~" + tweet[i]
	if len(text) > 0:
		prepareFeatures(text)

f.close()
conn.close()