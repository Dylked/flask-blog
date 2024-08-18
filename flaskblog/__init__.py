import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ce47795775b2691bdf733fc320684c73'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='587',
MAIL_USE_TLS=True,
MAIL_USERNAME=os.environ.get('EMAIL_USER'),
MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
)
mail = Mail(app)

from flaskblog import routes
