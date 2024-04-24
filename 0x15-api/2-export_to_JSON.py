#!/usr/bin/python3
"""
Extend Previous script to export data
JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}/users/{}'
    todo_str = '{}/todos?userId={}'
    # fetch response code
    user_res = requests.get(user_str.format(url, user_id))
    # get response body
    username = user_res.json().get('username')
    todo_res = requests.get(todo_str.format(url, user_id))
    todo_str = todo_res.json()
    tasks = []
    for values in todo_str:
        tasks.append({"task": values.get('title'),
                      "completed": values.get('completed'),
                      "username": username})
    user_info = {}
    user_info[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(user_info, f)
