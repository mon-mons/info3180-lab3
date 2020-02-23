from flask_wtf import FlaskForm 
from wtforms import StringField 
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm): 
     name= StringField('Name', validators=[DataRequired()])
     email= StringField('E-mail', validators=[DataRequired(),Email()])
     subject= StringField('Subject', validators=[DataRequired()])
     txt_area=TextAreaField('Message', validators=[DataRequired()])

     






     



