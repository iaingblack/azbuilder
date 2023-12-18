# WTF -- add length validator

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import IntegerField, DecimalField
from wtforms.validators import InputRequired, Length

class SimpleForm(FlaskForm):
   # added a validator
   name=StringField("name", 
   validators=[InputRequired(message="You must enter a name"), 
               Length(min=3, 
                      max=20, 
                      message="Name length must be between 3 and 20 characters")])
   # if the browser handles the error, you won't see this message

   submit = SubmitField("Enter")
   # http://wtforms.simplecodes.com/docs/0.6.1/fields.html
   language = SelectField(u'Programming Language', 
   choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
   
   color = SelectField(u'Color Choice', 
   choices=[('#FF0000', 'red'),
   ('#00FF00','green'),
   ('#0000FF','blue')])
   
   hours=IntegerField("hours", 
                      validators=[InputRequired()], 
                      render_kw={"value": "20" })
   
   wage = DecimalField("wage", 
                       validators=[InputRequired()], 
                       render_kw={"step": "0.05", "min" : "7.25", "value": "10.00" })