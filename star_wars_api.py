import requests
import pprint
import json
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from operator import itemgetter


pp = pprint.PrettyPrinter(indent=4)

response = requests.get("https://swapi.dev/api/starships/")
data = response.json()
#pprint.pprint(data)

starship_keys = []

for i in data['results']:
    #Here, I wanted the user to be able to sort using any key. since I don't know if each dictionary has the exact same keys, I'll iterate through all the dictionaries in the response and add each key to the list if it does not exist in the list already
    key_list = i.keys()
    for x in key_list:
        #print(x)
        if x not in starship_keys:
            starship_keys.append(x)


print(f'Which value would you like to sort by? You can sort by:')
print(*starship_keys, sep=", ")
user_input = input()

flagname = False
while not flagname:
    if user_input in starship_keys:
        flagname = True
    else:
        print('This input is not valid. please enter one of the following:')
        print(*starship_keys, sep=", ")
        user_input = input()

#Reference: https://www.easypythondocs.com/validation.html


newlist = sorted(data["results"], key=itemgetter(f'{user_input}')) 

names = [ item['name'] for item in newlist]
print(names)





