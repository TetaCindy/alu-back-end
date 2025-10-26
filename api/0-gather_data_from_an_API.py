#!/usr/bin/python3
"""
Module that uses a REST API to return information about an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Safely get employee name
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task.get("title") for task in todos_data if task.get("completed")]

    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Print output in required format
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for title in completed_tasks:
        print("\t {}".format(title))

