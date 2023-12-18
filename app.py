import string
import random

from flask import Flask, render_template
from wtforms import StringField
from wtforms.validators import DataRequired

from dominate.tags import *
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

default_location = "northeurope"
# Resources we can create
resource_types = ['vnet', 'nsg', 'pip']
# Required, Optional, Checkbox
# resource_params = [
#     ([],[],[])
# ]

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
    return render_template("pages/home.html", locations=simple_locations(json_locations()), resource_types=resource_types, default_location=default_location)

@app.route('/resource/new')
def resource_new_get():  # put application's code here
    return render_template("pages/home.html", locations=simple_locations(json_locations()), resource_types=resource_types, default_location=default_location)

@app.route('/randomword', methods=['GET'])
def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

# @app.route('/add_new_resource', methods=['GET'])
@app.route('/add_new_resource/<resource_type>', methods=['GET', 'POST'])
def add_new_resource(resource_type):
    # letters = string.ascii_lowercase
    # return ''.join(random.choice(letters) for i in range(10))
    select = request.form.get('resource_type')
    return('{}'.format(resource_type))

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

# https://flask-wtf.readthedocs.io/en/1.2.x/quickstart/#
class MyForm():
    name = StringField('name', validators=[DataRequired()])

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == '__main__':
    # Get the available Azure Locations into a list
    app.run(host="0.0.0.0", port=8000, debug=True)
