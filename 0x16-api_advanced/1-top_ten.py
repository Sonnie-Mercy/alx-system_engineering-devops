#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """prints the titles of the 1st 10 posts for a given sub"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my-user-agent'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    else:
        print(None)
