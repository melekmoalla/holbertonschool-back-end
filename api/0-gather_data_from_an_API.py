#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her
list progress.
Requirements:
You must use urllib or requests module
The script must accept an integer as a parameter, which is
the employee ID
The script must display on the standard output the employee
list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

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
