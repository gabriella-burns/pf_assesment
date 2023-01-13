import requests
import pprint
from flask import Flask, request, redirect, session, jsonify
import json
from operator import itemgetter
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'


def merge(names, values):
    
    merged_list = [(names[i], values[i]) for i in range(0, len(values))]
    return merged_list

@app.route('/', methods = ['GET', 'POST'])
def get_data():
    response = requests.get("https://swapi.dev/api/starships/")
    data = response.json()
    session["data"] = data
    return redirect("/sort")

@app.route('/sort', methods = ['GET', 'POST'])
def sort():
    data = session.get('data')
    starship_keys = []

    #Here, I wanted the user to be able to sort using any key. since I don't know if each dictionary has the exact same keys, I'll iterate through all the dictionaries in the response and add each key to the list if it does not exist in the list already
    for i in data['results']:
        key_list = i.keys()
        for x in key_list:
            #print(x)
            if x not in starship_keys:
                starship_keys.append(x)


    print(f'Which value would you like to sort by? You can sort by:')
    print(*starship_keys, sep=", ")
    user_input = input()

    #This ensures a user's input is valid by checking to see if their input is in the list of keys
    flagname = False
    while not flagname:
        if user_input in starship_keys:
            flagname = True
        else:
            print('This input is not valid. please enter one of the following:')
            print(*starship_keys, sep=", ")
            user_input = input()
   # return jsonify(user_input)
    session["user_input"] = user_input
    return redirect('/order')

@app.route('/order', methods = ['GET', 'POST'])
def order():
    data = session.get('data')
    user_input = session.get('user_input')
    print("would you like to sort in ascending or descending order")

    sort_order = input()

    if sort_order == "ascending":
        newlist = sorted(data["results"], key=itemgetter(f'{user_input}')) 
    elif sort_order == "descending":
        newlist = sorted(data["results"], key=itemgetter(f'{user_input}'), reverse = True)     
    else:
        "sorry, your input was not valid. Please enter either ascending or descending."
        sort_order = input()
        if sort_order == "ascending":
            newlist = sorted(data["results"], key=itemgetter(f'{user_input}')) 
        elif sort_order == "descending":
            newlist = sorted(data["results"], key=itemgetter(f'{user_input}'), reverse = True)   

    names = [ item['name'] for item in newlist]
    values = [ item[f'{user_input}'] for item in newlist]

    sorted_list= merge(names, values)

    #for i in sorted_list:
       # f'{i[0]}: {i[1]}'
    return(sorted_list)
    #print(names)

if __name__ == '__main__':
    app.run(debug=True)





