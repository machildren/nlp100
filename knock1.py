#!/usr/bin/python
#-*-coding:utf-8-*-
"""
excution
python knock1.py
"""

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys

def main():
	"""
	main function
	"""
    num_line = 0
    for line in open(sys.argv[1]):
        num_line += 1
    print num_line

if __name__ == "__main__":
    main()
