#!/usr/bin/python
# -*-cording:utf-8-*-

"""
execute
python knock4.py col1.txt col2.txt
"""
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys

def main():
 	"""
 	main function
 	"""
 	list_main = []
	list1 = []
	list2 = []
	f1 = open('coladd.txt','w')
	for line1 in open(sys.argv[1]):
	    line1 = line1.strip()
	    list1.append(line1)
	for line2 in open(sys.argv[2]):
	    line2 = line2.strip()
	    list2.append(line2)
	for i in range(len(list1)):
	    list_main = list1[i] + '\t' +list2[i]
	    f1.write('%s\n' %list_main)
if __name__ == '__main__':
	main()