#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock18.py tweet.txt
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
    re_sity_address = re.compile(u'仙台市[一-龠]{1,10}')
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
    return (tweet_dict, re_sity_address)
def judge_sity_address(tweet_dict, re_sity_address):
    """
    judge sity_address or not
    """
    for key, value in tweet_dict.items():
        for tweet_match in value:
            sity_address = re_sity_address.search(tweet_match.decode('utf-8'))
            if sity_address is None:
                pass
            else:
                print sity_address.group()
if __name__ == '__main__':
    tweet_dict, re_sity_address = get_tweet()
    judge_sity_address(tweet_dict, re_sity_address)

