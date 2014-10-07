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
			# chuck strings of digits and empty strings
			if item == "" or item[0] in "0123456789":
				continue
			hist[item] = hist.get(item, 0) + 1
	
	# invert histogram
	inverse = {}
	for key in hist:
		val = hist[key]
		inverse.setdefault(val,[]).append(key)
	print inverse

if __name__ == "__main__":
	main()