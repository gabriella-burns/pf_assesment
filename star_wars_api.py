import requests
import pprint
from flask import Flask, request, redirect, session, jsonify, render_template
import json
from operator import itemgetter
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'


def build_starship_array(data, starship_keys):
    for i in data['results']:
        key_list = i.keys()
        for x in key_list:
            #print(x)
            if x not in starship_keys:
                starship_keys.append(x)

def get_data():
    response = requests.get("https://swapi.dev/api/starships/")
    starship_keys = []

    data = response.json()
    build_starship_array(data, starship_keys)
    #loop that calls endpoint until it's done, shove everything in dictionary 
    while data["next"] != None:
        print(data["next"])
        response = requests.get(data["next"])
        data = response.json()
        build_starship_array(data, starship_keys)
    
    return starship_keys


# having an attribute different than what you sort by could be easier 
# named tuples (could use for headers in the 4 loop)

#Here, I wanted the user to be able to sort using any key. since I don't know if each dictionary has the exact same keys, I'll iterate through all the dictionaries in the response and add each key to the list if it does not exist in the list already

#Return template and data
#define a function that takes in data


def merge(names, values):
    
    merged_list = [(names[i], values[i]) for i in range(0, len(values))]
    return merged_list

@app.route("/")
def index():

    return render_template("index.html", starship_keys=get_data())

@app.route("/")
@app.route('/starships', methods = ['POST'])
def starships():
    data = get_data()

    sort_value = request.form["starship_value"]
    sort_order = request.form["sort_by"]

    if sort_order == "Ascending":
        newlist = sorted(data["results"], key=itemgetter(f'{sort_value}'))
    elif sort_order == "Descending":
        newlist = sorted(data["results"], key=itemgetter(f'{sort_value}'), reverse = True)     

    names = [ item['name'] for item in newlist]
    values = [ item[f'{sort_value}'] for item in newlist]

    sorted_list= merge(names, values)

    return render_template("index.html", sorted_list=sorted_list, starship_keys=data, sort_value=sort_value)
    #print(names)

if __name__ == '__main__':
    app.run(debug=True)





