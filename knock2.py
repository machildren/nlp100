#!/usr/bin/python
#-*-coding:utf-8-*-

"""
excution
python knock2.py
"""

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys

def main():
	"""
	main function
	"""
	for line in open(sys.argv[1]):
		print line.replace("	"," ").strip()

if __name__ == '__main__':
	main()
