#!/usr/bin/python3
"""
Script that fetches data from the JSONPlaceholder API.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users/{}"

    user_url = base_url.format(employee_id)
    todos_url = "{}/todos".format(user_url)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    employee_name = user_response.json().get('name')
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed') is True]

    print("Employee {} is done with tasks({}/{})"
          .format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))

