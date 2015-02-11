#!/usr/bin/python
# coding:utf-8

import sys
import argparse
from lxml import etree

__author__ = "@machildren & yossy"
__version__ = "0.0"
#(92) １番目の文のlemmaを並べたもの

def getArgs():
	# パーサーの生成
	parser = argparse.ArgumentParser(description="xml parse")

	# オプション引数の追加
	parser.add_argument(
		"-f", "--file",
		dest="xml_file",
		required=True,
		help="xml形式のファイル"
	)
	return parser.parse_args()


if __name__ == "__main__":
	args = getArgs()
	tree = etree.parse(args.xml_file)
	root = tree.getroot()
	build_text_list = etree.XPath("//text()")
	lemma_list = []
	for s_element in root.iter("sentence"):
		if "id" in s_element.attrib:
			if s_element.attrib["id"] == "1":
				for l_element in s_element.iter("lemma"):
					lemma_list.append(l_element.text)
	#print lemma_list
	print " ".join(lemma_list)