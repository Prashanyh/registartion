# Importing require libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

# Database Configuration and Creating object of SQLAlchemy

# app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# Create User Model which contains id [Auto Generated], name, username, email and password

class User(db.Model):

    __tablename__ = 'usertable'

    id = db.Column(db.Integer, primary_key=True)

    name= db.Column(db.String(15), unique=True)

    username = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256), unique=True)
