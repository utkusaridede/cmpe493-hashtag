import json

tweets_data_path = '../trash/dataset1.json'

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
	hash_index = [pos for pos, char in enumerate(tw_text) if char == '#']
	space_index = [pos for pos, char in enumerate(tw_text) if char == ' ']

	spaceCounter = 0
	hashtagList = []
	for i in range(0,len(hash_index)):
		for k in range(0,len(space_index)):

			if i < len(hash_index)-1:
				if hash_index[i+1] > space_index[spaceCounter] and hash_index[i] > space_index[spaceCounter]:
					spaceCounter += 1
				elif hash_index[i+1] > space_index[spaceCounter] and hash_index[i] < space_index[spaceCounter]:
					hashTag = tw_text[hash_index[i]+1:space_index[spaceCounter]]
					if len(hashTag) != 0:
						hashtagList.append(hashTag)
					break
				else:
					hashtag = tw_text[hash_index[i]+1:hash_index[i+1]]
					if len(hashTag) != 0:
						hashtagList.append(hashTag)
					break
			else:
				if hash_index[i] > space_index[spaceCounter]:
					spaceCounter += 1
				else:
					hashTag = tw_text[hash_index[i]+1:space_index[spaceCounter]]
					if len(hashTag) != 0:
						hashtagList.append(hashTag)
					break
	print(hashtagList)
	#print(tw_text)