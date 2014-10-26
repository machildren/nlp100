#!/usr/bin/python
# -*-coding:utf-8-*-
"""
excution
python knock3.py address.txt
"""

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys
def main():
	"""
	main function
	"""
	f1 = open('col1.txt','w')
	f2 = open('col2.txt','w')
	text = open(sys.argv[1])
	for line in text:
		itemList = line[:-1].split('\t')
		f1.write('%s\n' %itemList[0])
		f2.write('%s\n' %itemList[1])
	f1.close()
	f2.close()

if __name__ == '__main__':
	main()
