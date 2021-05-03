#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    new_list = []
    for key in posts:
        new_dict = {}
        USER_ID = key.get('userId')
        t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(USER_ID).json()
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(USER_ID)).json()
        new_dict["username"] = r.get('username')
        new_dict["task"] = t.get('title')
        new_dict["completed"] = t.get('completed')
        new_list.append(new_dict)
        json_dict = {}
        json_dict[USER_ID] = new_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
