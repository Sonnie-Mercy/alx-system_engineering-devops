#!/usr/bin/python3
""" imports data in JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(userId)).json()
    uname = u.get("username")
    task = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": uname
            } for t in task]}, jsonfile)
