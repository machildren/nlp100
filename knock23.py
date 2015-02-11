#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

__author__ = "@machildren"
__version__ = "1.0"


def main():
	for line in open('medline2.txt'):
		for list_word in line.strip().split(" "):
			print list_word
		print

if __name__ == "__main__":
    main()