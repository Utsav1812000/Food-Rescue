from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server = True

app = Flask(__name__)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

db = SQLAlchemy(app)

class User_details(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(25), nullable=False)
    Last_name = db.Column(db.String(25), nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password= db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(16), nullable=True)

@app.route("/")
def start():
    return render_template('login.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('F:/contact_form/contactform.html')

@app.route("/signup", methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        '''Add entry to the database'''
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        mobile= request.form.get('mobile')
        email = request.form.get('email')
        password= request.form.get('password')
        entry=User_details(First_name=fname, Last_name=lname, mobile=mobile, email=email, password=password, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('signup.html')

app.run(debug=True)