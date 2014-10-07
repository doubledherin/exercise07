from sys import argv

script, filename = argv

hist = {}

fin = open(filename)
for line in fin:
	line = line.rstrip().split()
	print line