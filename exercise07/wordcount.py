import string
from sys import argv

script, filename = argv

def main():
	hist = {}

	exclude = string.punctuation

	fin = open(filename)
	for line in fin:	
		# get rid of punctuation
		line = ''.join(char for char in line if char not in exclude)
		# lowercase, dump newlines, and split into a list of word strings
		line = line.lower().rstrip().split(" ")

		# build histogram
		for item in line:
			hist[item] = hist.get(item, 0) + 1
	
	for key, value in hist.iteritems():
		print key, value

if __name__ == "__main__":
	main()