#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
__author__ = "@machildren"
__version__ = "1.0"
def main():
	for line in open('medline2.txt'):
		for list_word in line.strip().split(" "):
			if list_word[-1] in [".", ",","(",")"]:
				print "%s\n%s" % (list_word[:-1], list_word[-1])
			else:
				print list_word

if __name__ == "__main__":
    main()