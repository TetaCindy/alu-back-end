#!/usr/bin/python3
"""
Exports all tasks of an employee in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    # Build list of task dictionaries in correct key order
    tasks = []
for todo in todos_data:
    tasks.append({
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": username
    })


    data = {str(user_id): tasks}

    # Write JSON file
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)
