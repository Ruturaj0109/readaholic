from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_33'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

data = {
    "website_name": "Readaholic",
    "Author" : "Ruturaj Jadhav"
}

db= SQLAlchemy(app)

bcrypt = Bcrypt(app)

from readaholic import routes