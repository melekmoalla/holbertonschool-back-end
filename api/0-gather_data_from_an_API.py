#!/usr/bin/python3
import requests
import sys



# Retrieve employee data
employee_id = int(sys.argv[1])
employee_data = requests.get(f"https://jsonplaceholder.typicode.com/users?id={employee_id}").json()
employee_name = employee_data[0]["name"]


# Retrieve todo list for employee
todos_data = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()
# Calculate progress
total_tasks = len(todos_data)
completed_tasks = len([task for task in todos_data if task["completed"]== True])
progress = f"{completed_tasks}/{total_tasks}"

# Print progress and completed tasks
print(f"Employee {employee_name} is done with tasks({progress}):")
for task in todos_data:
    if task["completed"] == True:
        print(f"\t {task['title']}")
