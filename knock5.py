#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock5.py col1.txt col2.txt
"""
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys

def main():
	text_line = list()
	length = int(raw_input())
	for line in open(sys.argv[1]):
		text_line.append(line)
	for i in range(length):
		print text_line[i].strip()


if __name__ == '__main__':
	main()
