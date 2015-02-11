#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from stemming.porter2 import stem


__author__ = "@machildren"
__version__ = "1.0"


def knock30():
	for line in sys.stdin:
		print "%s\t%s\t%s" % (line.strip().split()[0], line.strip().split()[1], stem(line.strip().split()[1]))
if __name__ == "__main__":
    knock30()