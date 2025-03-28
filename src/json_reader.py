import json


def read_json(filename):
    with open(filename, "r") as f:
        users = json.load(f)
    return users
