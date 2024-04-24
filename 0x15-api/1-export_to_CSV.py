#!/usr/bin/python3
"""create a csv file from
an API result """
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'
    todo_str = '{}todos?userId={}'
    # get username
    user = requests.get(user_str.format(url, user_id))
    user_name = user.json().get('username')
    # list of all the tasks
    todo_list = requests.get(todo_str.format(url, user_id))
    tasks = []
    todo_json = todo_list.json()
    for task_info in todo_json:
        tasks.append([user_id, user_name, task_info.get('completed'),
                      task_info.get('title')])
    with open("{}.csv".format(user_id),
              'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow(task)
