import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

response = requests.get("https://swapi.dev/api/starships/")
data = response.json()
pprint.pprint(data)

names = []

for i in data['results']:
    names.append(i['name'])

names.sort()

print(names)

