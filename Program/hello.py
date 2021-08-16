from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, tudy!</p>"

@app.route("/<name>")
def hello(name):
    navigation = [
        {"href": "/", "caption": "home"},
        {"href": "/Michael", "caption": "This but with Michael"}
    ]
    return render_template("hello.html.jinja", navigation=navigation)
