#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + employee_id)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

    employee = response.json()
    todos = todos.json()
    id = employee['id']
    name = employee['username']
    som = []
    for i in todos:
            m = []
            TASK_COMPLETED_STATUS = i['completed']
            TASK_TITLE = i['title']
            m.append(f"{id}")
            m.append(name)
            m.append(str(TASK_COMPLETED_STATUS))
            m.append(TASK_TITLE)
            som.append(m)

    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(som)





