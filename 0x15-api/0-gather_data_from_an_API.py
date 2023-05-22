#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_resp = requests.get(employee_url)
    employee_data = employee_resp.json()
    emp_name = employee_data.get("name")
    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    t_resp = requests.get(t_url)
    t_data = t_resp.json()

    tasks = len(t_data)
    comp = [todo for todo in t_data if todo.get("completed")]
    num_comp = len(comp)

    print(f"Employee {emp_name} is done with tasks({num_comp}/{tasks}):")
    for task in comp:
        print("\t", task.get("title"))
