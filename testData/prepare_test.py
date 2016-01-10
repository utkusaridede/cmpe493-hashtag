
def prepareFeaturesTest(text):

	textSize = len(text)
	for i in range(0, textSize):
		# Feature 1
		f.write("m1=")
		for j in range(0,3):
			if i+j < textSize:
				if text[i+j] in "0123456789":
						f.write(text[i+j])
				else:
					f.write(text[i+j].lower())
			else:
				f.write("@")
		f.write(" ")
		# Feature 2
		f.write("m2=")
		for j in range(0,3):
			if i+j < textSize:
				f.write(text[i+j])
			else:
				f.write("@")
		f.write(" ")
		# Feature 3
		f.write("m3=")
		for j in range(0,3):
			if i+j < textSize:
				if text[i+j] in "0123456789":
					f.write("#")
				else:
					if text[i+j].islower():
						f.write("x")
					elif text[i+j].isupper():
						f.write("X")
			else:
				f.write("@")
		f.write(" ")
		# Feature 4
		f.write("m4=")
		if i-1 < 0:
			f.write("@")
		else:
			if text[i-1] in "0123456789":
				f.write("#")
			else:
				if text[i-1].islower():
					f.write("x")
				elif text[i-1].isupper():
					f.write("X")

		if text[i] in "0123456789":
			f.write("#")
		else:	
			if text[i].islower():
				f.write("x")
			elif text[i].isupper():
				f.write("X")
		if i+1 < textSize:
			if text[i+1] in "0123456789":
				f.write("#")
			else:	
				if text[i+1].islower():
					f.write("x")
				elif text[i+1].isupper():
					f.write("X")
		else:
			f.write("@")
		f.write("\n")

f = open('randomHashtag.txt', 'w')

hashtag = "alinin2gözüayşesi"

prepareFeaturesTest(hashtag)

f.close()