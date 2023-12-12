# azgui
Gui for creating resources with az cli


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
pip install pyinstaller
pyinstaller -F -w -n azgui azgui.py
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
