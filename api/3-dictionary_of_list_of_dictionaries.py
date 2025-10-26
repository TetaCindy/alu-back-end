#!/usr/bin/python3
"""
Exports all tasks of all employees in JSON format.
"""

import json
import requests


def main():
    """Fetches users and their todos, then saves to JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users_response.raise_for_status()
    users_data = users_response.json()

    # Map user ID (as string) to username
    user_map = {str(user['id']): user['username'] for user in users_data}

    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Build dictionary: user_id (str) -> list of tasks
    output_dict = {}
    for todo in todos_data:
        user_id = str(todo['userId'])
        task_dict = {
            "username": user_map[user_id],
            "task": todo['title'],
            "completed": todo['completed']
        }
        output_dict.setdefault(user_id, []).append(task_dict)
    # Save to JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(output_dict, f)


if __name__ == "__main__":
    main()
