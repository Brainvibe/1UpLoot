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
@app.route('/get_games')
def get_games():
    return render_template("games.html", games=mongo.db.games.find(), genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
         port=os.environ.get('PORT'),
         debug=True)
