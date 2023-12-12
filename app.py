from flask import Flask, render_template
from dominate.tags import *

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("pages/home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
