#!/usr/bin/python3
""" fetching API"""
from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = {'id': argv[1]}
    id_todo = {'userId': argv[1]}
    employee_str = "Employee {} is done with tasks"
    res = get('https://jsonplaceholder.typicode.com/users'\
        , params=user_id)
    todo_res = get('https://jsonplaceholder.typicode.com/todos'\
        , params=id_todo)
    
