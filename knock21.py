#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

__author__ = "@machildren"
__version__ = "1.0"

def main():
	for line in open('medline.txt'):
		for line2 in line.strip().rstrip('.').split(". "):
			print line2 + '.'

if __name__ == "__main__":
    main()