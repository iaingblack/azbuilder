import string
import random

from flask import Flask, render_template
from dominate.tags import *
import json

app = Flask(__name__)

# Resources we can create
resources = ['vnet', 'nsg', 'pip']

def json_locations():
    with open('./static/locations.json') as locations_file:
        file_contents = locations_file.read()
        return json.loads(file_contents)

def simple_locations(locations:list) -> list:
    simple_locations = []
    for item in locations:
        simple_locations.append(item['name'])
    simple_locations_set = set(simple_locations)
    return sorted(list(simple_locations_set))

@app.route('/')
def root():  # put application's code here
    default_location = "northeurope"
    return render_template("pages/home.html", locations=simple_locations(json_locations()), resources=resources, default_location=default_location)

@app.route('/resource/new')
def resource_new_get():  # put application's code here
    return render_template("pages/home.html", locations=simple_locations(json_locations()), resources=resources, default_location=default_location)

@app.route('/randomword', methods=['GET'])
def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

if __name__ == '__main__':
    # Get the available Azure Locations into a list
    app.run(host="0.0.0.0", port=8000, debug=True)
