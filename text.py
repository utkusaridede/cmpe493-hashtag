import json

tweets_data_path = '../trash/tweetdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#print len(tweets_data)
tw = tweets_data[1]
tw_text = tw['text']
print [pos for pos, char in enumerate(tw_text) if char == '#']
#for tw in tweets_data:
#	print tw['text']