from flask import Flask, flash, redirect, render_template, request, session

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/About_us")
def about():
    return render_template("Aboutus.html")

@app.route("/Donate")
def about():
    return render_template("Donate.html")

@app.route("/Contact")
def about():
    return render_template("Contact.html")
