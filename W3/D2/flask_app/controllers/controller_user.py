from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_game import Game

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

'''
CRUD 
1. '/user'
2. '/user/<id>'
3. '/user/new' -> display route
4. '/user/create'
5. '/user/<user_id>/edit' -> display route
6. '/user/<user_id>/update'
7. '/user/<user_id>/delete'
'''

@app.route('/user')
def all_users():
    pass

@app.route('/user/<int:id>')
def one_user(id):
    context = {
        "user": User.get_one(id),
        "users_games": Game.get_users_all(id)
    }
    return render_template('user_info.html', **context)

# Display Route
@app.route('/user/new')
def new_user():
    pass

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect('/register')

    # bcrypt
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])

    info = {
        **request.form,
        "hash_pw": hash_pw
    }
    user_id = User.create(info)

    session['uuid'] = user_id
    return redirect('/')

# Display Route
@app.route('/user/<int:id>/edit')
def edit_user(id):
    context = {
        'user': User.get_one(id)
    }
    return render_template('edit_user.html', **context)

@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    user =  User.get_one(session['uuid'])
    print(user)
    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "hash_pw": user.hash_pw,
        "id": session['uuid'],
    }
    User.update_one(info)
    return redirect('/')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_one(id)
    return redirect('/logout')