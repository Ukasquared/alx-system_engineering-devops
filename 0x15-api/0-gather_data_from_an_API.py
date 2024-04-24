#!/usr/bin/python3
""" fetching API"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_res = '{}users/{}'.format(url_str, user_id)
    todos_res = '{}todos?userId={}'.format(url_str, user_id)
    employee_str = "Employee {} is done with tasks"

    res = requests.get(user_res)
    print(employee_str.format(res.json().get('name')), end="")

    res_todo = requests.get(todos_str)
    tasks = []
    for task in res.json():
        if task.get('completed') is True:
            tasks.append(task)

    print("({}/{}):".format(len(tasks), len(res.json())))
    for task in tasks:
        print("\t {}".format(task.get("title")))
