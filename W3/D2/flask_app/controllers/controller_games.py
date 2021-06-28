from logging import info
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.model_game import Game

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

'''
CRUD 
1. '/game'
2. '/game/<id>'
3. '/game/new' -> display route
4. '/game/create'
5. '/game/<game_id>/edit' -> display route
6. '/game/<game_id>/update'
7. '/game/<game_id>/delete'
'''

@app.route('/game')
def all_games():
    pass

@app.route('/game/<int:id>')
def one_game():
    pass

@app.route('/game/create', methods=['POST'])
def create_game():
    is_valid = Game.validate_game(request.form)
    if not is_valid:
        return redirect('/register')


    info = {
        **request.form,
        "user_id": session['uuid']
    }
    game_id = Game.create(info)

    return jsonify(message="game added")

# Display Route
@app.route('/game/<int:id>/edit')
def edit_game(id):
    context = {
        'game': Game.get_one(id)
    }
    return render_template('edit_game.html', **context)

@app.route('/game/<int:id>/update', methods=['POST'])
def update_game(id):
    game =  Game.get_one(id)
    info = {
        "name": request.form['name'],
        "id": id,
    }
    game.update_one(info)
    return redirect('/')

@app.route('/game/<int:id>/delete/')
def delete_game(id):
    game = Game.get_one(id)
    user_id = game.user_id
    Game.delete_one(id)
    return redirect(f'/user/{user_id}')

@app.route('/game/<int:game_id>/like')
def like_game(game_id):
    game = Game.get_one(game_id)
    info = {
        "name": game.name,
        "likes": game.likes + 1,
        "id": game_id
    }
    Game.update_one(info)
    return jsonify(message="success")

@app.route('/game/<int:game_id>/unlike')
def unlike_game(game_id):
    game = Game.get_one(game_id)
    info = {
        "name": game.name,
        "likes": game.likes - 1,
        "id": game_id
    }
    Game.update_one(info)
    return redirect('/')