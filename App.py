import os
import boto3
import logging
from flask import Flask
from flask import render_template

LOCAL_IMAGES = 'static'
IMAGES_SOURCE = os.getenv('IMAGES_SOURCE')
BUCKET_NAME = 'images-cloud-storage'

logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)

def clear_files():
    for filename in os.listdir(LOCAL_IMAGES):
        file_path = os.path.join(LOCAL_IMAGES, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def download_files():
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='')
    if 'Contents' not in response:
        return
    for obj in response['Contents']:
        s3_key = obj['Key']
        local_path = os.path.join(LOCAL_IMAGES, s3_key)
        s3.download_file(BUCKET_NAME, s3_key, local_path)

def get_local_images():
    if IMAGES_SOURCE == 'local':
        return [img for img in os.listdir(LOCAL_IMAGES)]
    elif IMAGES_SOURCE == 's3':
        clear_files()
        download_files()
        return [img for img in os.listdir(LOCAL_IMAGES)]
    return []

@app.route("/")
def get_menu():
    return render_template('Main.html', images=get_local_images())