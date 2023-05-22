#!/usr/bin/python3
"""
Script that uses REST API for fetching employee TODO progress
and exports data to CSV.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_endpoint = "{}users/{}".format(url, employee_id)
    todo_endpoint = "{}todos".format(url)

    user = requests.get(user_endpoint).json()
    todos = requests.get(todo_endpoint, params={"userId": employee_id}).json()

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            row = [employee_id,
                   user.get('username'),
                   task.get('completed'),
                   task.get('title')]
            taskwriter.writerow(row)
