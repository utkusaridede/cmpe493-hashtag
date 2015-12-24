#!/usr/bin/python

import re, sys

t = 0
totals = 0
totalh = 0
p = 0
r = 0
n = 0

def countEntry(segmented, trueSegmentation):
    global totals, totalh, r, p, n, t
    
    sw = segmented.split(' ')
    hw = trueSegmentation.split(' ')
    for s in sw:
        for h in hw:
            if s.lower() == h.lower():
                p = p + 1
                break
    for h in hw:
        for s in sw:
            if s.lower() == h.lower():
                r = r + 1
                break
            
    totals = totals + len(sw)
    totalh = totalh + len(hw)
    n += 1
    
    if segmented == trueSegmentation:
        t += 1
    
def calculatePrecision():
    if totals > 0:
        return ((float)(p*100)/(float)(totals))
    return 0

def calculateRecall():
    if totalh > 0:
        return ((float)(r*100)/(float)(totalh))
    return 0

def calculateFScore():
    precision = calculatePrecision()
    recall = calculateRecall()
    
    if precision+recall > 0:
        return 2*precision*recall/(precision+recall)
    return 0

def calculateAccuracy():
    if n > 0:
        return ((float)(100*t)/(float)(n))
    return 0

for arg in sys.argv:
    if re.search(".py$", arg) == None:
        f = open(arg)
        lines = f.readlines()
        f.close()
        for line in lines:
            line = re.sub("\n", "", line)
            fields = line.split("\t")
            if len(fields) == 2:
                countEntry(fields[1], fields[0])
            else:
                print "ERR: Invalid line '%s'" % (line)
                exit(0)

print "PRECISION = %.2f" % calculatePrecision()
print "RECALL = %.2f" % calculateRecall()
print "FSCORE = %.2f" % calculateFScore()
print "ACCURACY = %.2f" % calculateAccuracy()
