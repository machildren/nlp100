#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock17.py tweet.txt
"""

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/10/24"

import sys
import re
from collections import defaultdict
def get_tweet():
    """
    get tweet function
    """
    tweet = ''
    account = ''

    tweet_dict = defaultdict(list)
    re_account = re.compile(r'([0-9a-zA-Z_]{1,15}) : ')
    re_name = re.compile(u'([一-龥ぁ-んァ-ヴ]{1,4})(君|ちゃん|氏|さん|殿)')

    for line in open(sys.argv[1]):
        result_match = re_account.match(line)
        if result_match is None:
            tweet = tweet + line
        else:
            if account == '':
                pass
            else:
                tweet = tweet[:-1]
                tweet_dict[account].append(tweet)
            account = result_match.group(1)
            tweet = line[len(result_match.group()):]
    return (tweet_dict, re_name)
def judge_name(tweet_dict, re_name):
    """
    judge name or not
    """
    for key, value in tweet_dict.items():
        for tweet_match in value:
            tweet_match = tweet_match.decode('utf-8')
            like_name = re_name.search(tweet_match)
            if like_name is None:
                pass
            else:
                print like_name.group(0).encode('utf-8')
if __name__ == '__main__':
    tweet_dict, re_name = get_tweet()
    judge_name(tweet_dict, re_name)

