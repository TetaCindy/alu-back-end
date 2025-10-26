#!/usr/bin/python3
"""
Module that exports data in the CSV format for a given employee ID.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data.get("username")

    # Fetch TODO list
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    response = requests.get(todos_url)
    todos_data = response.json()

    # Write data to CSV
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

