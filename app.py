
from flask import Flask, json, render_template, redirect, request, session, url_for
from flask_session import Session
from flask_pymongo import PyMongo

from db import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/breeds")
def breedsView(): 
    # breeds = getAllMainBreeds()          
    return render_template('main_breeds.html', breeds=[{"_id":1,"name":"unnamed-1", "canTalk":True, "desc": "desc 1", "numSpecies":3},{"_id":2,"name":"unnamed-1", "canTalk":True, "desc": "desc 1", "numSpecies":3},{"_id":3,"name":"unnamed-1", "canTalk":True, "desc": "desc 1", "numSpecies":3},{"_id":4,"name":"unnamed-1", "canTalk":True, "desc": "desc 1", "numSpecies":3},{"_id":5,"name":"unnamed-1", "canTalk":True, "desc": "desc 1", "numSpecies":3}])

@app.route("/breeds/<breed_name>")
def subBreedsView(breed_name):        
    # subBreeds = getSubSpecies(breed_name)
    # print("birdInfo:", birdInfo[:])    
    return render_template('sub_breeds.html', subBreeds=[{}])

@app.route("/breeds/<species_name>")
def bird_infoView(species_name):
    bird = species_name
    return render_template('bird_info.html',bird=bird)

#app.add_url_rule('/breeds/<bird_name>', 'bird_infoView', bird_infoView) 

@app.route("/blogs")
def blogView():
    return render_template('blog.html')

@app.route("/about us")
def about_us():
    return render_template('about_us.html')

# Thai

@app.route("/TH/")
def index_TH():
    return render_template('index-TH.html')

@app.route("/TH/breeds")
def productView_TH():
    return render_template('product-TH.html')

@app.route("/TH/blogs")
def blogView_TH():
    return render_template('blog-TH.html')

@app.route("/TH/about us")
def about_us_TH():
    return render_template('about_us-TH.html')

# China


# Ajax
@app.route("/_add_bird")
def addBirdtoDB():
    name = request.args.get('name')
    image = request.args.get('image')
    result = addBirdInfo([{'name':name,'image':image}])
    return result.status

if __name__ == "__main__":
    app.run(debug=True)