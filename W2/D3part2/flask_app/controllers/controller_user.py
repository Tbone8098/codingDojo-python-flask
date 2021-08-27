from werkzeug.utils import redirect
from flask_app import app
from flask import render_template, redirect, session

from flask_app.models.model_user import User
from flask_app.models.model_fav_food import FavFood

@app.route("/")
def index():
    session['uuid'] = 5 # id of whoever's logged in
    # call the get all classmethod to get all friends
    one_user = User.get_one(session['uuid'])
    print(one_user)
    return render_template("index.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

'''
"/users/new" -> display the page with the form to create the new user
"/users/create" -> 'INSERT INTO ... '
"/users/update"
"/users/delete"

"/fav_food/<int:id>"
"/fav_food/new"
"/fav_food/create"
"/fav_food/update"
"/fav_food/delete"

'''