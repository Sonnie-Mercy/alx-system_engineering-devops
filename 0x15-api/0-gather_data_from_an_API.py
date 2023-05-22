#!/usr/bin/python3
"""
A script that uses REST API to fetch employee TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]

    # Retrieve employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_resp = requests.get(employee_url)
    employee_data = employee_resp.json()
    emp_name = employee_data.get("name")

    # Retrieve employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_resp = requests.get(todos_url)
    todos_data = todos_resp.json()

    tasks = len(todos_data)
    comp = [todo for todo in todos_data if todo.get("completed")]
    num_comp = len(comp)

    print(f"Employee {emp_name} is done with tasks({num_comp}/{tasks}):")
    for task in comp:
        print("\t", task.get("title"))
