#!/usr/bin/python
# -*- coding: utf-8 -*-

#knock22

import sys
import re

__author__ = "@machildren"
__version__ = "1.0"
__date__ = "2014/09/22"
__update__  = "2014/12/12"

def main():
	for line in sys.stdin:
		line = line.strip()
		print re.sub(r'\. ([A-Z])', r'.\n\1', line)
if __name__ == "__main__":
    main()