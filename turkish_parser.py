import json
tweets = []

for line in open('../trash/dataset1.json'):
	try: 
		tweets.append(json.loads(line))
	except:
		pass

print len(tweets)

tweet = tweets[6]

#.decode('iso-8859-9').encode('utf8')
#texts = []
#for tweet in tweets:
#	texts.append(tweet['text'])

texts = open("texts.txt", "wb")

for x in xrange(0,len(tweets)-1):
	tweet = tweets[x]
	print tweet['text']