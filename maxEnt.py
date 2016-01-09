
from subprocess import call

learningData = "deneme.txt"

call(["maxent", learningData, "-m", "model", "-i", "30", "--gis"])

test = "test.txt"
output = "output.txt"

call(["maxent", "-p", test, "-m", "model", "-o", output])