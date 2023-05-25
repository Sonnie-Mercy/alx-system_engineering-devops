#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import cvs
import requests
import sys

if __name__ == "__main__":
    """utilizing CVS and REST API"""

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if response.status_code != 200:
        sys.exit(1)

    todos = response.json()
    employee_name = todos[0]["name"]
    task_data = []
    for todo in todos:
        task_data.append({
            "USER_ID": employee_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": str(todo["completed"]),
            "TASK_TITLE": todo["title"]
        })

    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow
        (["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in task_data:
            writer.writerow(task.values())
