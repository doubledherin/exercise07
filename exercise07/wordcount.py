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
	
	# invert histogram, so key = frequency and value = list of words
	inverse = {}
	for key in hist:
		val = hist[key]
		inverse.setdefault(val,[]).append(key)

	# convert inverted histo into list of tuples sorted by descending frequency
	inverse_pairs = sorted(inverse.items(), reverse=True)
	
	# loop through list of tuples, sorting words for each one & printing
	for pair in inverse_pairs:
		words = sorted(pair[1])
		for word in words:
			print "%s: %r" % (word, pair[0])



if __name__ == "__main__":
	main()