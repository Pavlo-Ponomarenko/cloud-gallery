from flask import Flask
from procedures import *
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def get_menu():
    return render_template('Main.html')