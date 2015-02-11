# !usr/bin/python
# coding:utf-8
import sys
from knock10 import *


__author__ = "@machildren"
__version__ = "1.0"


def knock27():
	wordlist=[]
	for word in open('medline4.txt'):
		wordlist.append(word)
	main(wordlist)

if __name__ == '__main__':
	knock27()