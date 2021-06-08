from datetime import date
from os import name
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql6417974:vyFM7VIHgU@sql6.freemysqlhosting.net/sql6417974'
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('index.html')

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    message = db.Column(db.String(153), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=False)


@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method=='POST' :
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, email=email, phone=phone, message=message, date=datetime.now())

        db.session.add(entry)
        db.session.commit()


    return render_template('contact.html')


app.run(debug=True)