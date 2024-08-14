#!/usr/bin/python3
"""contains `top_ten` function"""
import requests as req


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    header = {'user-agent': 'chrome'}
    param = {'limit': 10}
    res = req.get(url, allow_redirects=False, headers=header, params=param)
    if res.status_code == 200:
        data = res.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
