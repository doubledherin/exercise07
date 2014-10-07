from sys import argv

script, filename = argv

def main():
	hist = {}

	fin = open(filename)
	for line in fin:
		line = line.rstrip().split(" ")
		for item in line:
			hist[item] = hist.get(item, 0) + 1
	
	for key, value in hist.iteritems():
		print key, value

if __name__ == "__main__":
	main()