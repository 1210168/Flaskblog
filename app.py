from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import tkinter as tk
from tkinter import messagebox

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    body=db.Column(db.String(300),nullable=False)
    created_at=db.Column(db.DateTime,nullable=False,default=datetime.now(pytz.timezone("Asia/Tokyo")))

@app.route("/",methods=["GET"])  #変更
def index():
    posts = Post.query.all()   #DBに登録した内容をすべて取得する
    return render_template("index.html",posts=posts)

@app.route("/article1")
def article1():
    return render_template("article1.html")

@app.route("/article2")
def article2():
    return render_template("article2.html")

@app.route("/create",methods=["GET","POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        
        post = Post(title=title,body=body)
        
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("create.html")

@app.route("/<int:id>/update",methods=["GET","POST"])   #DBのIDがルーティングの部分に持ってこれるように指定する
def update(id):
    post=Post.query.get(id)
    if request.method == "GET":
        return render_template("update.html",post=post)
    else:
        post.title = request.form.get("title")
        post.body = request.form.get("body")
        db.session.commit()
        return redirect("/")

@app.route("/<int:id>/delete",methods=["GET"])
def delete(id):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()
    res = messagebox.askokcancel("確認", "投稿を削除しますか？")
    if res == True:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
    root.destroy()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)