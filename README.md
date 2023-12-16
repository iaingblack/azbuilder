# AZ Builder
Webapp for creating resources with az cli. It will be a simple pick a resource and fill in the options. It can take quite a long time to figure out the required info for every resource when you want to quickly architect something. AZ CLI is a great way to do prototyping without needing to dive into powershell cmdlets (perhaps a nice alternative), ARM templates (ugh!), Ansible (okay for simple things), Terraform (high initial effort), etc...

# Example

This seems like a great example of what could be done. Python and Flask Backend, with HTMX to make adding 'resources' via HTML blocks (buttons, dropdowns, checkbox etc) and then I can generate the az cli command (somehow) from it. HTMX means I dont need React etc... I had no idea client side generation of a dynamic web 'GUI' like this without state could be so difficult (though I could be missing something).

https://codecapsules.io/tutorial/building-a-full-stack-application-with-flask-and-htmx/


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