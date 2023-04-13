#!/usr/bin/python3
""" Gather data from an API """
import requests as r
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    todo = r.get("https://jsonplaceholder.typicode.com/todos")
    name = r.get("https://jsonplaceholder.typicode.com/users/" + id)
    data = todo.json()
    done = 0
    total = 0
    tasks = []
    for d in data:
        if d.get("userId") == int(id):
            if d.get("completed"):
                tasks.append(d.get("title"))
                done += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):".format(
          name.json().get('name'), done, total))
    for task in tasks:
        print("\t {}".format(task))
