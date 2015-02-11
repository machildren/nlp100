#!/usr/bin/python
# -*- coding: utf-8 -*-
\
import sys
import re

__author__ = "@machildren"
__version__ = "1.0"


def main():
	for line in open('medline.txt'):
		line = line.strip()
		print re.sub(r'\. ([A-Z])', r'.\n\1', line)
if __name__ == "__main__":
    main()