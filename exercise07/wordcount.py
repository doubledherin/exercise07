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
			# chuck strings of digits
			if item.isdigit() or item == "":
				continue
			hist[item] = hist.get(item, 0) + 1
	
	hist_items = hist.items()
	hist_items.sort(reverse=True)
	print hist_items

if __name__ == "__main__":
	main()