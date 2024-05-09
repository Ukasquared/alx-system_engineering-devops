#!/usr/bin/python3
"""
retieves the subscriber count for
a specific subreddit
"""
import requests

def top_ten(subreddit):
    """ retrieve number of
    for a particular subreddit
    """
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/124.0.0.0 Safari/537.36"}
    end_point = "r/{}/hot.json".format(subreddit)
    url = "https://www.reddit.com/{}".format(end_point)
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 301:
            print ("None")
        to_json = response.json()
        # get data key
        data_list = to_json.get("data").get("children")
        for i in range(0, 9):
            post_title = data_list[i].get("data").get("title")
            print (post_title)
    except Exception:
        print ("None")
