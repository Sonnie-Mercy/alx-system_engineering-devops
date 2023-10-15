#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list of titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of
    all hot articles for a given subreddit
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', None)
        if data:
            for post in data:
                hot_list.append(post['data']['title'])
            after = response.json().get('data', {}).get('after', None)
            if after is not None:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            for title in result:
                print(title)
        else:
            print("None")
