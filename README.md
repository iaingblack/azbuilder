# AZ Builder
Webapp for creating resources with az cli. It will be a simple pick a resource and fill in the options. It can take quite a long time to figure out the required info for every resource when you want to quickly architect something. AZ CLI is a great way to do prototyping without needing to dive into powershell cmdlets (perhaps a nice alternative), ARM templates (ugh!), Ansible (okay for simple things), Terraform (high initial effort), etc...

# Example

This seems like a great example of what could be done. Python and Flask Backend, with HTMX to make adding 'resources' via HTML blocks (buttons, dropdowns, checkbox etc) and then I can generate the az cli command (somehow) from it. HTMX means I dont need React etc... I had no idea client side generation of a dynamic web 'GUI' like this without state could be so difficult (though I could be missing something).
Actually, it isnt as bad as I thought, you can do anything you like, but it forces a page reload. So I can do whatever I need without HTMX, but it isnt as 'nice'. I can still maintain state through the python variables being passed around.

https://codecapsules.io/tutorial/building-a-full-stack-application-with-flask-and-htmx/

Also good
https://apostrophecms.com/blog/htmx-examples-and-how-to-use-it

## Python Setup

Just for my reference. How to setup a virtual env and test a build of the installer on windows.

Download and unzip repo

### Mac/Ubuntu 22.04

```bash
sudo apt install python3 python3-pip python3-venv python3-tk -y
python3 -m venv ./venv/
sudo chmod +x ./venv/bin/activate
. ./venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 azgui.py
```

Mac
```
brew install python-tk
```

Requirements
```bash
pip3 freeze > requirements.txt
```

Django
Create Project (one time)
```bash
django-admin startproject azbuilder .
```
Start Server
```bash
python3 manage.py runserver 
```

# Pages Required
What do I need to be able to do?
 - Set the location and RG name
 - Add a resource
 - Delete a Resource
 - Edit a Resource (maybe too much)
 - Generate a command line script from the choices

It may be required that I make an object or a page per resource. That would suck. Ideally I want a way to make a generic object and have the values it can accept (required, optional, checkboxes for things), then generate a table of input fields based on that. 

# Static Data

Locations
```bash
az account list-locations -o json > ./static/locations.json
```

https://stackoverflow.com/questions/2733813/iterating-through-a-json-object
```python
with open('./static/locations.json') as locations_file:
  file_contents = locations_file.read()
```