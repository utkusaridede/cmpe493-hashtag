#!/usr/bin/python
# -*- coding: utf8 -*-
import sqlite3
import codecs

f = codecs.open('randomHastag.txt', 'w', 'utf-8')
conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute("SELECT * FROM HASHTAGS")
rows = c.fetchall()
counter = 0
for row in rows:
	if len(row[1]) > 16: 
		f.write(row[1])
		f.write('\n')
		counter = counter + 1
#print counter
f.close()
conn.close()