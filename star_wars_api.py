import requests
import pprint
from flask import Flask, request, redirect, session, jsonify, render_template
import json
from operator import itemgetter
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'



def get_urls():
    url_list = ["https://swapi.dev/api/starships/"]
    response = requests.get("https://swapi.dev/api/starships/")
    data = response.json()
    while data["next"] != None:
        #print(data["next"])
        url=data["next"]
        url_list.append(url)
        response = requests.get(data["next"])
        data = response.json()
    #print(url_list)

    return url_list

def get_data():
    url_list = get_urls()
    dict_list = []
    for url in url_list:
        response = requests.get(url)
        data = response.json()
        results = data["results"]
        dict_list.append(results)
        #print(f'dict list:{dict_list}')
    data = json.dumps(dict_list, indent =2)
    return data


# def get_keys(starship_keys):
#     data = get_data()
#     data_j = json.dump(data)
#     #print(f'data: {data}')
#     for i in data_j:
#         print(i)
#         key_list = i.keys()
#         #print(key_list)
#         for x in key_list:
#             #print(x)
#             if x not in starship_keys:
#                 starship_keys.append(x)
#     return starship_keys
def get_keys():  
    starship_keys = []
    response = requests.get("https://swapi.dev/api/starships/")
    data = response.json()       
    for i in data["results"]:
        key_list = i.keys()
        #print(key_list)
        for x in key_list:
            print(x)
            if x not in starship_keys:
                starship_keys.append(x)
    return starship_keys

get_urls()

get_data()
get_keys()

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

    return render_template("index.html", starship_keys=get_keys())

@app.route("/")
@app.route('/starships', methods = ['POST'])
def starships():

    data = get_data()
    print(data)

    sort_value = request.form["starship_value"]
    sort_order = request.form["sort_by"]

    if sort_order == "Ascending":
        newlist = sorted(data, key=itemgetter(f'{sort_value}'))
    elif sort_order == "Descending":
        newlist = sorted(data, key=itemgetter(f'{sort_value}'), reverse = True)     

    names = [ item['name'] for item in newlist]
    values = [ item[f'{sort_value}'] for item in newlist]

    sorted_list= merge(names, values)

    return render_template("index.html", sorted_list=sorted_list, starship_keys=data, sort_value=sort_value)
    #print(names)

if __name__ == '__main__':
    app.run(debug=True)





