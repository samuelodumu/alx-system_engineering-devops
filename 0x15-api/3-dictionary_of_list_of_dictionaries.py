#!/usr/bin/python3
"""returns information about a given employee's TODO list progress"""
import json
import requests
import sys

'''
Pseudo-code
1. start
2. create a dictionary (dict1)
3. for user_id in range(1, 11): # so that the id is dynamic
        a. add the id to dict1 and set it to an empty list []
        b. for each todo:
                i. create a new dictionary (dict2)
                ii. add the username, task name and completed status
                    fields to dict2 as appropriate
                iii. append dict2 to the list
4. open 'todo_all_employees.json' for writing
5. dump dict1 with json into it
6. end
'''

if __name__ == '__main__':
    file_name = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/"

    all_users_dict = {}
    for user_id in range(1, 11):
        users = f"users/{user_id}"
        todos = f"todos?userId={user_id}"
        user_data = requests.get(f"{url}{users}").json()
        user_todos_data = requests.get(f"{url}{todos}").json()
        all_users_dict[user_id] = []
        for todo in user_todos_data:
            json_line = {}
            json_line["username"] = user_data["username"]
            json_line["task"] = todo["title"]
            json_line["completed"] = todo["completed"]
            all_users_dict[user_id] += [json_line]

    with open(file_name, "w") as f:
        json.dump(all_users_dict, f)
