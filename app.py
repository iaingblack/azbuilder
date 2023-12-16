from flask import Flask, render_template
from dominate.tags import *
import json

app = Flask(__name__)

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
def hello_world():  # put application's code here
    resources = ['rg','nsg','vnet']
    default_location = "northeurope"
    return render_template("pages/home.html", locations=simple_locations(json_locations()), resources=resources, default_location=default_location)

@app.route('/random', methods=['GET'])
def random():
    html = '<p>dfsdfsdfsdf</p>'
    print(html)
    return html

if __name__ == '__main__':
    # Get the available Azure Locations into a list
    app.run(host="0.0.0.0", port=8000, debug=True)
