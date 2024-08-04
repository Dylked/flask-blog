from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ce47795775b2691bdf733fc320684c73'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)

from flaskblog import routes