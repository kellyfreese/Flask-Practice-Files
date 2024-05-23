from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"
db = SQLAlchemy(app)

class Villain(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(80), unique=True, nullable=False)
  description=db.Column(db.String(250), unique=False, nullable=False)
  interests=db.Column(db.String(250), unique=False, nullable=False)
  url=db.Column(db.String(250), unique=False, nullable=False)
  date_added=db.Column(db.DateTime, unique=False, nullable-False, default.utcnow)

def __repr__(self):
  return "<Villain " +self.name + ">"

@app.route("/")
def hello_world():
  return render_template("villain.html")


app.run(host='0.0.0.0', port=8080)