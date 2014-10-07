from sys import argv

script, filename = argv

hist = {}

fin = open(filename)
for line in fin:
	line = line.rstrip().split(" ")
	for item in line:
		hist[item] = hist.get(item, 0) + 1
print hist
