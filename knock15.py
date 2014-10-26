
#!/usr/bin/python
# -*-coding:utf-8-*-
"""
execute
python knock15.py tweet.txt
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
    re_at_user = re.compile(r"@([0-9a-zA-Z_]{1,15})")

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
    return (tweet_dict, re_at_user)
def replace_user_url(tweet_dict, re_at_user):
    """
    replace user_url
    """
    for key, value in tweet_dict.items():
        for tweet_match in value:
            at_user = re_at_user.search(tweet_match)
            if at_user is None:
                pass
            else:
                print '<ahref=\'https://twitter.com/#!/\'' + at_user.group(1) + '>' + at_user.group(0) + '</a>'
if __name__ == '__main__':
    tweet_dict, re_at_user = get_tweet()
    replace_user_url(tweet_dict, re_at_user)

