#!/usr/bin/python3
"""
Extend Previous script to export data
JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}/users/'
    todo_str = '{}/todos'
    # fetch response code
    user_res = requests.get(user_str.format(url))
    # get response body
    user_name = user_res.json()
    todo_res = requests.get(todo_str.format(url))
    todo_str = todo_res.json()
    user_info = {}
    for user in user_name:
        tasks = []
        username = user.get('username')
        userId = user.get('id')
        for task in todo_str:
            if task.get('userId') == userId:
                tasks.append({"username": username,
                              "task": task.get('title'),
                              "completed": task.get('completed')})
        user_info[userId] = tasks
    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_info, f)
