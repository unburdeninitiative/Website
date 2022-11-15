from flask import Flask, flash, redirect, render_template, request, session

app= Flask(__name__)

@app.route("/", endpoint='home')
def home():
    return render_template("homepage.html")

@app.route("/Aboutus.html",endpoint='about')
def about():
    return render_template("Aboutus.html")

@app.route("/Donate.html",endpoint='donate')
def donate():
    return render_template("Donate.html")

@app.route("/Contact.html",endpoint='contact')
def contact():
    return render_template("Contact.html")