#!/usr/bin/python3
"""Using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(userId)).json()
    uname = u.get("username")
    task = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            userId, uname, t.get("completed"), t.get("title")]) for t in task
