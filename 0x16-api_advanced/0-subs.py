#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """If an invalid subreddit is given, the function should return 0"""
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    r = requests.get("https://www.reddit.com/r/{}/.json".format(subreddit))
    if r.status_code == 404:
        return 0
    else:
        r = r.json()
        subscribers = r.get('subreddit_subscribers')
        return subscribers

