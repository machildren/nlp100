#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock16.py tweet.txt
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
    re_uppercase = re.compile(r'([一-龠])+\(([A-Z]+)\)')

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
    return (tweet_dict, re_uppercase)
def uppercase(tweet_dict, re_uppercase):
    """
    replace user_url
    """
    for key, value in tweet_dict.items():
        for tweet_match in value:
            uppercase = re_uppercase.search(tweet_match)
            if uppercase is None:
                pass
            else:
                print uppercase.group(0)
if __name__ == '__main__':
    tweet_dict, re_uppercase = get_tweet()
    uppercase(tweet_dict, re_uppercase)

