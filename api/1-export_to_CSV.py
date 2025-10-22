#!/usr/bin/python3
"""Exports an employee's TODO list data to CSV format"""

import csv
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
    username = user.get("username")

    # Get todos
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    # Write to CSV
    filename = "{}.csv".format(emp_id)
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

