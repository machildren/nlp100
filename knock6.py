#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock6.py col1.txt col2.txt
"""
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/24"

import sys

def main():
	"""
	main function
	"""
	length = int(raw_input())
	f = open(sys.argv[1])
	line = f.readlines()
	line.reverse()
	for i in range(length):
		print line[length-i-1].strip()
if __name__ == '__main__':
	main()
