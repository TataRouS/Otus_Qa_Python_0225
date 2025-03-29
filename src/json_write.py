import json


def write_json(filename, data):
    with open(filename, "a") as f:
        json.dump(data, f, indent=4)
