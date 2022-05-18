from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    body = db.Column(db.String(300),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now(pytz.timezone("Asia/Tokyo")))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/article1")
def article1():
    return render_template("article1.html")

@app.route("/article2")
def article2():
    return render_template("article2.html")

if __name__ == '__main__':
    app.run(debug=True)
