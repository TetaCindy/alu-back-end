#!/usr/bin/python3
"""
Module that uses a REST API to return information about
an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    response = requests.get(user_url)
    user_data = response.json()
    employee_name = user_data.get("name")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    response = requests.get(todos_url)
    todos_data = response.json()

    completed_tasks = [task.get("title") for task in todos_data
                       if task.get("completed")]

    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    for task_title in completed_tasks:
        print("\t {}".format(task_title))
