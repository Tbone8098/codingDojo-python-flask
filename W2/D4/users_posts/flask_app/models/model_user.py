from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE_SCHEMA = 'users_and_posts_db'

class User:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def create(cls, info):
        query = 'INSERT INTO users (username, first_name, last_name, email, pw) VALUES (%(username)s, %(first_name)s, %(last_name)s, %(email)s, %(hash_pw)s)'
        data = {
            "username": info['username'],
            "first_name": info['first_name'],
            "last_name": info['last_name'],
            "email": info['email'],
            "hash_pw": info['hash_pw'],
        }
        new_user_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return new_user_id
    
# R
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        data ={
            'id': id
        }
        return connectToMySQL(DATABASE_SCHEMA).query_db(query,data)[0]
    
    @classmethod
    def get_one_by_username(cls, username):
        query= 'SELECT * FROM users WHERE username = %(username)s;'
        data = {
            "username" : username
        }
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return result
    
    # Delete if not a user model
    @classmethod
    def get_one_by_email(cls, email):
        pass
# U
    @classmethod
    def update_one(cls, info):
        query = 'UPDATE users SET username=%(username)s, first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, pw=%(pw)s WHERE id=%(id)s'
        data = {
            "username": info['username'],
            "first_name": info['first_name'],
            "last_name": info['last_name'],
            "email": info['email'],
            "pw": info['pw'],
            "id": info['id'],
        }

        return connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

# D
    @classmethod
    def delete_one(cls, id):
        query = 'DELETE FROM users WHERE id=%(id)s'
        data = {
            "id": id
        }
        connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        print(f"user with the id {id} has been deleted")
        return id

    @staticmethod
    def validate_user(form_data):
        is_valid = True
        
        if len(form_data['first_name']) < 1:
            flash("Missing required first name. ")
            is_valid = False
        
        if len(form_data['first_name']) < 3:
            flash("First name must be greater than 3 characters. ")
            is_valid = False
        
        # if form_data['first_name'] != form_data['first_name'].upper():
        #     flash("MUST BE ALL UPPER CASE!")
        #     is_valid = False

        if len(form_data['last_name']) < 3:
            flash("Last name must be greater than 3 characters. ")
            is_valid = False

        if len(form_data['email']) < 3:
            flash("Email must be greater than 3 characters. ")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address")
            is_valid = False

        if len(form_data['username']) < 3:
            flash("Username must be greater than 3 characters. ")
            is_valid = False

        user = User.get_one_by_username(form_data['username'])
        if len(user) >= 1:
            flash("username is already taken")

        if len(form_data['pw']) < 8:
            flash("Password must be greater than 8 characters. ")
            is_valid = False
        
        return is_valid