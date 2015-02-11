#!/usr/bin/python
# coding:utf-8

import sys
import argparse
from lxml import etree

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


def main():
	tree = etree.parse(args.xml_file)
	root = tree.getroot()

	for k_element in root.iter("sentence"):
		if "id" in k_element.attrib:
			if k_element.attrib["id"] == "2":
				for kk_element in k_element.iter("token"):
					if "id" in kk_element.attrib:
						if kk_element.attrib["id"] == "5":
							for kkk_element in kk_element.iter("word"):
								print kkk_element.text

	build_text_list = root.XPath("//text()")
if __name__ == "__main__":
	args = getArgs()
	main()



