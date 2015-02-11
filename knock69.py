#!usr/bin/python
#-*-coding:utf-8-*-

import sys
__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/09/20"
print "graph knock69{"
for line in open(sys.argv[1]):
        list = line.strip().split("\t")
        print "\t\"" + list[1] + "\" -- \"" + list[2] + "\";"
print "}"