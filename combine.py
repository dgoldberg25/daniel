import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("index.html")

@app.route('/blog')
def blog():
	redirect("blog.html")

@app.route('/about')
def about():
	redirect("about.html")

@app.route('/contact')
def contact():
	redirect("contact.html")
