#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re
from knock54 import *
re_marks = re.compile(u"[。、「」『』]|。")
dst = ""
srcs = ""
noun_cnt = 0
noun2_cnt = 0
text = main()
for sent in text:
        for Ch in sent:
                for w in Ch.morphs:
                        if w.pos == "名詞":
                                noun_cnt += 1
                        if re_marks.search(w.surface.decode("utf-8")) is None:
                                        dst += w.surface
                for w in sent[Ch.dst].morphs:
                        if w.pos == "名詞":
                                noun2_cnt += 1
                        if re_marks.search(w.surface.decode("utf-8")) is None:
                                srcs += w.surface
                if noun_cnt != 0 and noun2_cnt != 0:
                        print dst + "\t" + srcs +"\t"+"[係り受けパス]:"+ str(Ch.ID) +">>>"+ str(Ch.dst)
                dst = ""
                srcs = ""
                noun_cnt = 0
                noun2_cnt = 0