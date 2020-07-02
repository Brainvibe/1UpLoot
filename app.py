import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = '1up_loot'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_games')
def get_games():
    return render_template("games.html", games=mongo.db.games.find(), genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())

@app.route('/add_games')
def add_games():
    return render_template("addgame.html",genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())

@app.route('/insert_game', methods=['POST'])
def insert_game():
    games = mongo.db.games
    games.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
         port=os.environ.get('PORT'),
         debug=True)
