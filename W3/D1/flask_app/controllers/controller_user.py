from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

@app.route('/')
def index():
    if 'lookup_user' not in session:
        session['lookup_user'] = 1
    return redirect('/users')

@app.route('/users')
def dashboard():
    context = {
        "all_users": User.get_all(),
        "user": User.get_one(session['lookup_user'])
    }
    return render_template('dashboard.html', **context)

@app.route('/users/create', methods=['POST'])
def create_user():
    user_id = User.create(request.form)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:id>')
def show_user(id):
    context = {
        "user": User.get_one(id) 
    }
    return render_template('show_user.html', **context)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    context = {
    "user": User.get_one(user_id)
    }

    return render_template('edit_user.html', **context)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    info = {
        **request.form,
        "id": user_id
    }
    User.update_one(info)
    return redirect(f'/users/{user_id}')

@app.route('/users/find', methods=['POST'])
def find_user():
    user_found = User.get_one_by_first_name(request.form['first_name'])
    print(user_found)
    session['lookup_user'] = user_found.id
    return redirect('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete_one(id)
    return redirect('/')