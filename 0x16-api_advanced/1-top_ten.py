#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for subcriber"""
import requests


def top_ten(subreddit):
        """Print the titles of the 10 subreddit."""
        u = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        h = {
            "User-Agent": "0x16-api_advanced:project:\
        v1.0.0 (by /u/firdaus_cartoon_jr)"
        }
        p = {
            "limit": 10
        }
        r = requests.get(u, h=h, p=p,
                                allow_redirects=False)
        if r.status_code == 404:
            print("None")
            return
        re = response.json().get("data")
        [print(c.get("data").get("title")) for c in re.get("children")]
