import xml.sax
import xml.sax.handler
import sys
import re

#(96) 記事のタイトルとカテゴリ情報．複数のカテゴリが設定されているときは，全て抜き出せ．

__author__ = "@machildren & yossy"
__version__ = "0.0"

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.frag = False
		self.frag_category = False
		self.category = ""
	def startElement(self, name, attrs):
		if name == "title":
			self.frag = True
		if name == "text":
			self.frag_category = True

	def endElement(self, name):
		if name == "title":
			self.frag = False
		if name == "text":
			self.frag_category = False
	def characters(self, content):
		if self.frag:
			self.title_name = content
		if self.frag_category:
			re_category_pattern = re.compile(r"(\[\[)(category:.+)(\]\])")
			match = re_category_pattern.search(content)
			if match:
				print "title:" + self.title_name.encode("utf-8")
				print match.group(2)
def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(sys.argv[1])
	return

if __name__=="__main__":
	main()