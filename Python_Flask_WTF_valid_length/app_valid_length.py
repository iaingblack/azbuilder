# WTF -- adding a length validator

# needs form_valid_length.py where SimpleForm class defined 
# needs simple_form_valid_length.html (templates) where HTML of form generated
# needs simple_form_valid_length_handler.html (templates) to display results
# needs simple_layout.htm (templates) and simple.css (static)

'''
   terminal commands: 
   cd venv
   Scripts/activate   (MAC/Linux: bin/activate)
   pip install flask-wtf  # if not already done
   $env:FLASK_APP = "app_valid_length"  #PowerShell version 
   $env:FLASK_DEBUG = "1"
   flask run
'''

from form_valid_length import SimpleForm
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# A SECRET_KEY
app.config["SECRET_KEY"]='why_a_duck?'

@app.route("/")
def my_redirect():
   return redirect(url_for('simple_form'))

@app.route('/simple_form', methods=['GET', 'POST'])
def simple_form():
   form = SimpleForm()
   print(form.validate_on_submit())
   #if form.is_submitted():
   if form.validate_on_submit():
      result = request.form
      return render_template('simple_form_valid_length_handler.html', 
                             title="Simple Form Handler", 
                             header="Simple form handler", 
                             result=result)
   return render_template('simple_form_valid_length.html', 
                          title="Simple Form", 
                          header="Simple form", 
                          form=form)

if __name__ == "__main__":
   app.run(debug=True)