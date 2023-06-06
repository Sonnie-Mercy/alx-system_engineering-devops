#!/usr/bin/python3
"""
queries the Reddit API and returs the hot articles of a sub
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    The function to use to recursively call to get hot articles in a sub
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my-user-agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')
    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
