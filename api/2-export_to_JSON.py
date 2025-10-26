#!/usr/bin/python3
"""
Exports data in JSON format for a given employee ID.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user and todos data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    # Prepare data in the required format
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {user_id: tasks}

    # Write data to JSON file
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)
