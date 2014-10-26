#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock8.py address.txt
"""
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/24"

import sys

def main():
	"""
	main function
	"""
	f = open(sys.argv[1])
	line = f.readlines()
	col = list()
	for itemList in line:
		itemList = itemList[:-1].split('\t')
		col.append(itemList)
	for i in sorted(col, key = lambda x:x[1]):
		print i[0], i[1]

if __name__ == '__main__':
	main()