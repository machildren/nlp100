#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

__author__ = "@machildren"
__version__ = "1.0"

def main():
    for word in open('medline3subl.txt'):
        print "%s\t%s" % (word.strip(), word.lower().strip())

if __name__ == "__main__":
    main()