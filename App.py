import os
from flask import Flask
from flask import render_template

LOCAL_IMAGES = "static"

app = Flask(__name__)

def get_local_images():
    return [img for img in os.listdir(LOCAL_IMAGES)]

@app.route("/")
def get_menu():
    return render_template('Main.html', images=get_local_images())