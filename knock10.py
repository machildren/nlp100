#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock10.py col2.txt
"""
__author__ = "@machildren"
__version__ = "1.0"

import sys
from collections import defaultdict
def main(f):
	"""
	main function
	"""
	d = defaultdict(int)
	#f = open(sys.argv[1])
	#line = f.readlines()
	line = f
	col = list()
	for col1 in line:
		col1 = col1.strip().split('\t')
		col.append(col1[0])
	for i in col:
		d[i] += 1
	for name, num in sorted(d.items(), key = lambda x:x[1], reverse = True):
		print name, num

if __name__ == '__main__':
	main(open(sys.argv[1]))