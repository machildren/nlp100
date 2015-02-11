#!/usr/bin/python
# coding:utf-8

import sys
import argparse
from lxml import etree

#(93) １番目の文の４番目のトークンの，係り受け構造上での子（dependent）の単語
__author__ = "@machildren & yossy"
__version__ = "0.0"

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

	for s_element in root.iter("sentence"):
		if "id" in s_element.attrib:
			if s_element.attrib["id"] == "1":
				for ds_element in s_element.iter("dependencies"):
					if "type" in ds_element.attrib:
						if ds_element.attrib["type"] == "basic-dependencies":
							for g_element in ds_element.iter("governor"):
								if "idx" in g_element.attrib:
									if g_element.attrib["idx"] == "4":
										for d_element in g_element.getparent().iter("dependent"):
											print d_element.text
#	print build_text_list(root)