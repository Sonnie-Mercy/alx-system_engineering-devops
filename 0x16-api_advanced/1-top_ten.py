#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', None)
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print("No data found for the subreddit.")
    else:
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
