#!/usr/bin/python3
"""
Module that queries the Reddit API and returns subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the no of subs for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
