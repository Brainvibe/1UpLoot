import os
import bcrypt
from os import path
from flask import Flask, render_template, redirect, request, url_for, session
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
    if 'username' in session:
        return render_template('index.html')
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
        
    if request.method == 'POST':
        login_user = users.find_one({'name' : request.form['username']})
        print(login_user)
        if login_user:
            if bcrypt.hashpw(request.form['pass'], login_user['password'] == login_user['password']):
               session['username'] = request.form['username']
            return redirect(url_for('index'))
            
        else:
            return 'Invalid username/password combination'
            
    return redirect(url_for('login'))
        
    
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name':request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Username already exists'
    return render_template('register.html')


@app.route('/get_games')
def get_games():
    return render_template("games.html", games=mongo.db.games.find(), genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())


@app.route('/get_search/<search>')
def get_search(search):
    plat_list = list(mongo.db.games.find({"platform_name": search}))
    return render_template("results.html", platforms=plat_list, games=mongo.db.games.find(), genres=mongo.db.genres.find())

@app.route('/search_genre/<genre>')
def search_genre(genre):
    genre_list = list(mongo.db.games.find({"genre_name": genre}))
    return render_template("results_genre.html", games=mongo.db.games.find(), genres=genre_list)

@app.route('/add_games')
def add_games():
    return render_template("addgame.html",genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())

@app.route('/insert_game', methods=['POST'])
def insert_game():
    games = mongo.db.games
    games.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))

@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    game_edit = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    genres=mongo.db.genres.find()
    platforms=mongo.db.platforms.find()
    return render_template('editgame.html', game=game_edit, genre=genres, plat=platforms)

@app.route('/update_game/<game_id>', methods=["POST"])
def update_game(game_id):
    games = mongo.db.games
    games.update( {'_id': ObjectId(game_id)},
    {
        'game_name':request.form.get('game_name'),
        'game_image':request.form.get('game_image'),
        'game_condition':request.form.get('game_condition'),
        'pickup_date':request.form.get('pickup_date'),
        'platform_name':request.form.get('platform_name'),
        'genre_name':request.form.get('genre_name')
    })
    return redirect(url_for('get_games'))

@app.route('/delete_task/<game_id>')
def delete_game(game_id):
    mongo.db.games.remove({'_id': ObjectId(game_id)})
    return redirect(url_for('get_games'))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
         port=os.environ.get('PORT'),
         debug=True)
         
