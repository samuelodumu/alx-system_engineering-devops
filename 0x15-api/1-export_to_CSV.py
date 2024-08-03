#!/usr/bin/python3
"""returns information about a given employee's TODO list progress"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    file_name = f'{employee_id}.csv'
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users?id={employee_id}'
    todos = f'todos?userId={employee_id}'
    user_data = requests.get(f"{url}{users}").json()
    user_todos_data = requests.get(f"{url}{todos}").json()

    employee_csv = ''
    for todo in user_todos_data:
        line = f'"{employee_id}","{user_data[0].get("username")}",'\
                f'"{todo.get("completed")}","{todo.get("title")}"\n'
        employee_csv += line

    with open(file_name, 'w') as f:
        f.write(employee_csv)
