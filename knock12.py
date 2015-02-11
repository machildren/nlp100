#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock12.py tweet.txt
"""

__author__ = "@machildren"
__version__ = "0.0"
__date__ = "2014/09/20"

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
    return tweet_dict

def judge_query_tweet(tweet_dict):
    for key, value in tweet_dict.items():
        for tweet_match in value:
            if re.search(r'なう$', tweet_match):
                print ('user_name : %s' %key)
                print '----------now_tweet----------------'
                print tweet_match
                print '-----------------------------------'
                print ''
            else:
                pass
if __name__ == '__main__':
    tweet_dict = get_tweet()
    judge_query_tweet(tweet_dict)