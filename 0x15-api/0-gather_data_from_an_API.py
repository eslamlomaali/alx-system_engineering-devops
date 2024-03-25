#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    objectt = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in objectt if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(objectt)))
    [print("\t {}".format(c)) for c in done]
