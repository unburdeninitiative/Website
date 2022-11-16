from flask import Flask, flash, redirect, render_template, request, session
from flask_frozen import Freezer

app= Flask(__name__)

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()


@app.route("/", endpoint='home')
def home():
    return render_template("Index.html")

@app.route("/Aboutus.html",endpoint='about')
def about():
    return render_template("Aboutus.html")

@app.route("/Donate.html",endpoint='donate')
def donate():
    return render_template("Donate.html")

@app.route("/Contact.html",endpoint='contact')
def contact():
    return render_template("Contact.html")
