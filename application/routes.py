from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/specs")
@app.route("/specifications")
def specs():
    return render_template("specs.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

