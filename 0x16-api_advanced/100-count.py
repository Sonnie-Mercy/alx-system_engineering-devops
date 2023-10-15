#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the titles of all hot
articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot
    articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): A token for pagination.
        word_count (dict): A dictionary to store the count of keywords.

    Returns:
        None
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
                title_words = post['data']['title'].lower().split()
                for word in word_list:
                    word_lower = word.lower()
                    if word_lower in title_words:
                        if word_lower in word_count:
                            word_count[word_lower] +=
                            title_words.count(word_lower)
                        else:
                            word_count[word_lower] =
                            title_words.count(word_lower)
            after = response.json().get('data', {}).get('after', None)
            if after is not None:
                count_words(subreddit, word_list, after, word_count)
            else:
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Please pass an
              argument for the subreddit and a list of keywords to search.")
    else:
        word_list = sys.argv[2:]
        count_words(sys.argv[1], word_list)
