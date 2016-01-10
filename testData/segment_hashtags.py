
testHashtag = open("testHashtag.txt", 'r')

BIresults = open("BIresults.txt", 'r')

segmented = open("manualSegmented.txt", 'r')

output = open("output.txt", 'w')

hastagLines = testHashtag.readlines()
BIlines = BIresults.readlines()
segmentLines = segmented.readlines()

index = 0
indexSeg = 0
for line in hastagLines:
	line = line.replace("\n", "")
	string = line
	space = 0
	for i in range(0, len(line)):
		if "B" in BIlines[i+index] and i != 0:
			string = string[:i+space] + " " + string[i+space:]
			space += 1
	index += len(line)
	lineSeg = segmentLines[indexSeg].replace("\n", "")
	output.write(lineSeg)
	output.write("\t")
	output.write(string)
	output.write("\n")
	indexSeg += 1