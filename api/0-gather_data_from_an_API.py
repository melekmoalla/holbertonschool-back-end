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


if __name__ == '__main__':

    import requests
    import sys

    employee_id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + employee_id)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

    employee = response.json()
    todos = todos.json()

    employee_name = employee['name']
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    completed_tasks_titles = [todo['title']
                              for todo in todos if todo['completed']]

    a = "is done with tasks"
    print(
        "Employee {} {}({}/{}):".format(employee_name, a, completed_tasks, total_tasks))
    for title in completed_tasks_titles:
        print("\t {}".format(title))
