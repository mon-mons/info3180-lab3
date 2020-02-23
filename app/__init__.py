
Learn more or give us feedback
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keepithush1442141255'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'b5eb613ea43686'
app.config['MAIL_PASSWORD'] = '41a7f1c4f0366e'
mail = Mail(app)

from app import views