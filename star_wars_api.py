import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

response = requests.get("https://swapi.dev/api/people/1/")
pprint.pprint(response.text)
