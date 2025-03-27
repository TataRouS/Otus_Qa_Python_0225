import json

data

with open("userbooks.json", a) as f:
    json.dump(data, f, indent=4)
