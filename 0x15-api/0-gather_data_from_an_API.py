#!/usr/bin/python3
"""
A script that uses REST API to fetch employee TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    employee = requests.get('{}/users/{}'.format(base_url, employee_id)).json()
    employee_name = employee.get('name')
    todos = requests.get('{}/todos'.format(base_url),
                         params={'userId': employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]

    # Output the employee's progress
    print('Employee {} is done with tasks({}/{})'.format(
        employee_name, len(done_tasks), total_tasks))

    # Output titles of completed tasks
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
