# jsnynglee website

import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session 
from tempfile import mkdtemp 


# configure application
app = Flask(__name__)


# configure cs50 library to use SQLite database
db = SQL("sqlite://project.db")


# make route to index 
@app.route("/")
def index():
    return render_template("index.html")


# make route to home 
@app.route("/home")
def home():
    return render_template("index.hthml")


# make route to about
@app.route("/about")
def about():
    return render_template("about.html")


# make route to education
@app.route("/education")
def education():
    return render_template("education.html")


# make route to work experience
@app.rout("/workexperience")
def workexperience():
    return render_template("workexperience.html")


# make route to hobbies
@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


# make route to film 
@app.route("/film")
def film():
    return render_template("film.html")

# make route to blog
@app.route("/blog")
def blog():
    return render_template("blog.html")

# make route to contact
@app.route("/contact")
def contact():
    return render_template("contact.html")