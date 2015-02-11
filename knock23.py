#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/25"

def main():
	for line in sys.stdin:
		for list_word in line.strip().split(" "):
			print list_word
		print

if __name__ == "__main__":
    main()