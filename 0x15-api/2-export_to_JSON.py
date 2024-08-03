#!/usr/bin/python3
"""returns information about a given employee's TODO list progress"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    file_name = f'{user_id}.json'
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users/{user_id}'
    todos = f'todos?userId={user_id}'
    user_data = requests.get(f'{url}{users}').json()
    user_todos_data = requests.get(f'{url}{todos}').json()

    user_dict = {f"{user_id}": []}
    for todo in user_todos_data:
        json_line = {}
        json_line[f"task"] = todo["title"]
        json_line[f"completed"] = todo[f"completed"]
        json_line[f"username"] = user_data[f"username"]
        user_dict[user_id] += [json_line]

    # print(user_dict)
    with open(file_name, "w") as f:
        json.dump(user_dict, f)

'''
{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}
'''
