#!/usr/bin/python3
"""
contains `recurse` method
"""
import requests


def recurse(subreddit, after=None):
    """returns a list containing the titles of all
    hot articles for a given subreddit"""
    headers = {"User-Agent": "Chrome"}
    params = {"after": after}
    url = f"https://www.reddit.com/r/subreddit/hot.json"
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
