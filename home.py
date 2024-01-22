import base64

from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session
from flask_pymongo import PyMongo

from db import *

app = Flask(__name__)

# Ajax
@app.route("/_add_bird")
def addBirdtoDB():

    name = request.args.get('name')
    image = request.args.get('image')
    file_path = image
    base64Image 
    try:
        with open(file_path, 'rb') as file:
            image_data = file.read()
            base64Image = base64.b64encode(image_data).decode('utf-8')
    except FileNotFoundError:
        base64Image = ''
    print(base64Image)
    # if base64Image != "":
        # result = addBirdInfo([{'name':name,'image':image}])
        # return result.status
    return False