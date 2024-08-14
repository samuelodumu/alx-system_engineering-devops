#!/usr/bin/python3
"""contains `number_of_subscribers` function"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-agent': 'chrome'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
