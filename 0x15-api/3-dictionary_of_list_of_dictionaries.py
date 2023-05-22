#!/usr/bin/python3
"""
Script that fetches data from the REST API for all employees
and exports data to a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_endpoint = url + "users"
    todos_endpoint = url + "todos"

    users_response = requests.get(users_endpoint)
    users_data = users_response.json()

    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    employee_tasks = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        user_tasks = []
        for task in todos_data:
            if task["userId"] == user_id:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                user_tasks.append(task_data)

        employee_tasks[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(employee_tasks, jsonfile)

    print("Data exported to:", filename)
