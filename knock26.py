# !usr/bin/python
# coding:utf-8
import sys
import re

__author__ = "@machildren"
__version__ = "1.0"


def main():
	re_nessly = re.compile("(ness|ly)$")
	for line in open('medline4.txt'):
		if re_nessly.search(line) != None:
			print line.strip()

if __name__ == '__main__':
	main()