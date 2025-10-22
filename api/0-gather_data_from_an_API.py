#!/usr/bin/env python3
"""
0-gather_data_from_an_API.py
Usage: python3 0-gather_data_from_an_API.py <employee_id>
Works even on Python 3.4 (no requests needed)
"""

import sys
import json
import urllib.request

API_BASE = "https://jsonplaceholder.typicode.com"

def get_json(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.", file=sys.stderr)
        sys.exit(1)

    # Fetch user info
    user_url = "{}/users/{}".format(API_BASE, emp_id)
    user = get_json(user_url)
    if not user or user == {}:
        print("Error: User with id {} not found.".format(emp_id), file=sys.stderr)
        sys.exit(1)

    employee_name = user.get("name", "Unknown")

    # Fetch todos
    todos_url = "{}/todos?userId={}".format(API_BASE, emp_id)
    todos = get_json(todos_url)
    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title", "")))

if __name__ == "__main__":
    main()

