import json

with open('data.json') as file:
    reader = json.load(file)
    print(reader)
