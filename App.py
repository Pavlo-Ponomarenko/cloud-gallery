import os
import logging
from flask import Flask
from flask import render_template

LOCAL_IMAGES = "static"

logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)

def get_local_images():
    return [img for img in os.listdir(LOCAL_IMAGES)]

@app.route("/")
def get_menu():
    return render_template('Main.html', images=get_local_images())