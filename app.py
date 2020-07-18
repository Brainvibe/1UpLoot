import os
import bcrypt
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, flash
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
        user = session['username']
        return render_template("index.html",user=user)
     else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index')) 
        else:
            error = 'Invalid username/password'
            return render_template('login.html',error_login=error)
    else:
        error = 'Invalid username/password'
        return render_template('login.html',error_login=error)

@app.route('/login_page')
def login_page():
     return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
          
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name':request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            error = 'Username already exists'
            return render_template('register.html',error_register=error)
    else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('index'))

@app.route('/<username>')
def user_games(username):
    if 'username' in session:
        user = session['username']
        return render_template("games.html", games=mongo.db.games.find(), genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find(), user=user)

@app.route('/get_search/<search>', methods=['POST'])
def get_search(search):
    if 'username' in session:
       user = session['username']
       plat_list = list(mongo.db.games.find({"platform_name": search, "user:":user}))
       print(plat_list)
       return render_template("results.html", user=user,platforms=plat_list, games=mongo.db.games.find(), genres=mongo.db.genres.find())
    else:
       return redirect(url_for('index'))

@app.route('/search_genre/<genre>')
def search_genre(genre):
  if 'username' in session:
    user = session['username']
    genre_list = list(mongo.db.games.find({"genre_name": genre,"user:":user}))
    print(genre_list)
    return render_template("results_genre.html", user=user, games=mongo.db.games.find(), genres=genre_list)
  else:
    return redirect(url_for('index'))
@app.route('/add_games')
def add_games():
   if 'username' in session:
      user = session['username']
    
      return render_template("addgame.html",games=mongo.db.games.find(),genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find(), user=user)
   else:
      return render_template("addgame.html",games=mongo.db.games.find(),genres=mongo.db.genres.find(), platforms=mongo.db.platforms.find())
    

@app.route('/insert_game', methods=['POST'])
def insert_game():
    user = session['username']
    games = mongo.db.games
    games.insert_one({
        'user': session['username'],
        'game_name':request.form.get('game_name'),
        'game_image':request.form.get('game_image'),
        'game_condition':request.form.get('game_condition'),
        'pickup_date':request.form.get('pickup_date'),
        'platform_name':request.form.get('platform_name'),
        'genre_name':request.form.get('genre_name'),
        'game_condition':request.form.get('game_condition'),
        'game_store':request.form.get('game_store'),
        'game_price':request.form.get('game_price'),
        'game_value':request.form.get('game_value'),
    })
    return redirect(url_for('user_games',username=user))

@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    user = session['username']
    game_edit = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    genres=mongo.db.genres.find()
    platforms=mongo.db.platforms.find()
    return render_template('editgame.html', user=user,game=game_edit, genre=genres, plat=platforms)

@app.route('/update_game/<game_id>', methods=["POST"])
def update_game(game_id):
    user = session['username']
    games = mongo.db.games
    games.update( {'_id': ObjectId(game_id)},
    {   
        'user': session['username'],
        'game_name':request.form.get('game_name'),
        'game_image':request.form.get('game_image'),
        'game_condition':request.form.get('game_condition'),
        'pickup_date':request.form.get('pickup_date'),
        'platform_name':request.form.get('platform_name'),
        'genre_name':request.form.get('genre_name'),
        'game_condition':request.form.get('game_condition'),
        'game_store':request.form.get('game_store'),
        'game_price':request.form.get('game_price'),
        'game_value':request.form.get('game_value'),
    })
    return redirect(url_for('user_games',username=user))

@app.route('/delete_task/<game_id>')
def delete_game(game_id):
    user = session['username']
    mongo.db.games.remove({'_id': ObjectId(game_id)})
    return redirect(url_for('user_games',username=user))

if __name__ == '__main__':
    
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
         port=os.environ.get('PORT'),
         debug=True)