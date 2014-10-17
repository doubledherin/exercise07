from sys import argv
import string

script, filename = argv

fin = open(filename)
content = fin.read().lower()
