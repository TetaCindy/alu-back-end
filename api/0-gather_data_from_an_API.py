#!/usr/bin/python3
"""Fetches and displays an employee TODO list progress from a REST API"""

import json
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    emp_id = int(sys.argv[1])

    # Get user info
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))
    employee_name = user.get("name")

    # Get todos
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    done_count = len(done_tasks)

    # Output
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

