#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock13.py tweet.txt
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
    re_RT = re.compile(r'RT @([0-9a-zA-Z_]{1,15}): ')

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
    return (tweet_dict, re_RT)
def judge_informal_RT_tweet(tweet_dict, re_RT):
    """
    judge infomal_RT or not
    """
    for key, value in tweet_dict.items():
        for tweet_match in value:
            RT = re_RT.match(tweet_match)
            if RT is None:
                RT = re_RT.search(tweet_match)
                if RT is None:
                    pass
                else:
                    print ('user_name : %s' %key)
                    print '----------informal_RT----------------'
                    print tweet_match[:RT.start()]
                    print '-------------------------------------'
                    print ''
            else:
                pass

if __name__ == '__main__':
    tweet_dict, re_RT = get_tweet()
    judge_informal_RT_tweet(tweet_dict, re_RT)

