from sys import argv

script, filename = argv

def main():
	hist = {}

	fin = open(filename)
	for line in fin:
		line = line.rstrip().split(" ")
		for item in line:
			hist[item] = hist.get(item, 0) + 1
	print hist

if __name__ == "__main__":
	main()