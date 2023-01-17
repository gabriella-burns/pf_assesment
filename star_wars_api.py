import requests
import pprint
from flask import Flask, request, redirect, session, jsonify, render_template
import json
from operator import itemgetter
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'

response = requests.get("https://swapi.dev/api/starships/")
data = response.json()

#data = session.get('data')


#Here, I wanted the user to be able to sort using any key. since I don't know if each dictionary has the exact same keys, I'll iterate through all the dictionaries in the response and add each key to the list if it does not exist in the list already
starship_keys = []

#Return template and data
for i in data['results']:
    key_list = i.keys()
    for x in key_list:
        #print(x)
        if x not in starship_keys:
            starship_keys.append(x)

def merge(names, values):
    
    merged_list = [(names[i], values[i]) for i in range(0, len(values))]
    return merged_list

@app.route("/")
def index():

    session["data"] = data
    session["starship_keys"] = starship_keys
    return render_template("index.html", starship_keys=starship_keys)

@app.route("/")
@app.route('/starships', methods = ['GET', 'POST'])
def starships():
    data = session.get('data')

    if request.method == 'POST':

        sort_value = request.form["starship_value"]
        sort_order = request.form["sort_by"]


        if sort_order == "Ascending":
            newlist = sorted(data["results"], key=itemgetter(f'{sort_value}')) 
        elif sort_order == "Descending":
            newlist = sorted(data["results"], key=itemgetter(f'{sort_value}'), reverse = True)     
       # else:
        #    "sorry, your input was not valid. Please enter either ascending or descending."
        #    sort_order = input()
        #    if sort_order == "ascending":
        #        newlist = sorted(data["results"], key=itemgetter(f'{sort_order}')) 
        #    elif sort_order == "descending":
        #        newlist = sorted(data["results"], key=itemgetter(f'{sort_order}'), reverse = True)   

        names = [ item['name'] for item in newlist]
        values = [ item[f'{sort_value}'] for item in newlist]

        sorted_list= merge(names, values)

        return render_template("results.html", sorted_list=sorted_list)
    #print(names)

if __name__ == '__main__':
    app.run(debug=True)





