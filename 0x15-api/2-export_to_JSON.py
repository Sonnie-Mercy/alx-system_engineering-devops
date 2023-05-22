#!/usr/bin/python3
"""
Script that fetches data from the REST API for a particular employee ID
and exports data to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_endpoint = "{}users/{}".format(url, employee_id)
    todo_endpoint = "{}todos".format(url)

    user = requests.get(user_endpoint).json()
    todos = requests.get(todo_endpoint, params={"userId": employee_id}).json()

    tasks = []
    for task in todos:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        }
        tasks.append(task_dict)

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
