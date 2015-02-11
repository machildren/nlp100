#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
#bigramとは任意の文字列が2文字だけ続いた文字列のことである
__author__ = "@machildren"
__version__ = "1.0"

def knock28():
	word = []
	bigram = []
	for line in open('medline4.txt'):
			list = line.strip().split("\t")
			word.append(list[1])
	for i in range(len(word)-1):
		bigram.append(word[i] + " " + word[i+1])
	for i in range(len(bigram)):
		print bigram[i]
	word_dict = defaultdict(lambda: 0)
	for w in bigram:
		word_dict[w] += 1
	for i, j in sorted(word_dict.items(), key = lambda x:-x[1]):
			print "%s\t%r" %(i, j)
if __name__ == '__main__':
	knock28()

