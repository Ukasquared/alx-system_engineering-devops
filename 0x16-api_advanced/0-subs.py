#!/usr/bin/python3
"""
retieves the subscriber count for
a specific subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """ retrieve number of
    for a particular subreddit
    """
    header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/124.0.0.0 Safari/537.36"}
    end_point = "r/{}/about.json".format(subreddit)
    url = "https://www.reddit.com/{}".format(end_point)
    #try:
    response = requests.get(url, headers=header)
    to_json = response.json()
    data = to_json.get("data")
    subscribers = data.get("subscribers")
    return subscribers
   # except Exception:
       # return 0
