from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/login')
def login():
    if 'uuid' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    # get the user by username
    list_of_users = User.get_one_by_username(request.form['username'])

    if len(list_of_users) <= 0:
        flash("no user found")
        return redirect('/login')

    user = list_of_users[0]
    print(user)
    if not bcrypt.check_password_hash(user['pw'], request.form['pw']):
        flash("Invalid Creds")
        return redirect('/login')
    
    session['uuid'] = user['id']
    return redirect('/')

@app.route('/register')
def register():
    if 'uuid' in session:
        return redirect('/')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')