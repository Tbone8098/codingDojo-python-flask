from typing import Protocol
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.model_user import User
import re

DATABASE_SCHEMA = 'users_games_db'

class Game:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.likes = data['likes']
        self.user_id = data['user_id']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']

    @property
    def game_to_user(self):
        return User.get_one(self.user_id)

    def __repr__(self) -> str:
        display = f"id: {self.id},  name: {self.name}, user_id: {self.user_id}, created_at: {self.created_at}, updated_at: {self.updated_at}"
        return display

# C
    @classmethod
    def create(cls, info):
        query = 'INSERT INTO games (name, user_id) VALUES (%(name)s, %(user_id)s)'
        data = {
            "name": info['name'],
            "user_id": info['user_id']
        }
        new_games_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return new_games_id
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM games'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)

        all_games = []
        for user in results:
            all_games.append(cls(user))

        return all_games

    @classmethod
    def get_users_all(cls, id):
        query = 'SELECT * FROM games WHERE user_id = %(user_id)s'
        data = {
            'user_id': id
        }
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

        all_games = []
        for user in results:
            all_games.append(cls(user))

        return all_games

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM games WHERE id = %(id)s;'
        data ={
            'id': id
        }
        return cls(connectToMySQL(DATABASE_SCHEMA).query_db(query,data)[0])

    
    # @classmethod
    # def get_one_by_email(cls, email):
    #     query= 'SELECT * FROM users WHERE email = %(email)s;'
    #     data = {
    #         "email" : email
    #     }

    #     result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data) # returns a list of dictionaries ( in this case only one dictionary)
        
    #     # if len(result) > 0:
    #     #     return cls(result[0])

    #     return result
    
    # Delete if not a user model
    # @classmethod
    # def get_one_by_email(cls, email):
    #     pass   
    #  

# U
    @classmethod
    def update_one(cls, info):
        # TODO: add the ability to update pw 
        query = 'UPDATE games SET name=%(name)s, likes=%(likes)s  WHERE id=%(id)s'
        data = {
            "name": info['name'],
            "likes": info['likes'],
            "id": info['id'],
        }

        return connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

# D
    @classmethod
    def delete_one(cls, id):
        query = 'DELETE FROM games WHERE id=%(id)s'
        data = {
            "id": id
        }
        connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        return id

    @staticmethod
    def validate_game(form_data):
        is_valid = True
        
        if len(form_data['name']) < 3:
            flash("Game name must be greater than 3 characters. ")
            is_valid = False
        
        return is_valid