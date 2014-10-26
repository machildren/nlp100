#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock9.py address.txt
"""
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/24"

import sys

def main():
	f = open(sys.argv[1])
	text = f.readlines()
	itemList = list()
	mainlist = list()
	for line in text:
		itemList = line[:-1].split('\t')
		mainlist.append(itemList)
	for i in sorted(mainlist, key = lambda x:(x[1], x[0]), reverse =True):
		print i[0],i[1]
if __name__ == '__main__':
	main()