from typing import ClassVar
from users_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,id,first_name,last_name,email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def get_all_users (cls):
        query = "Select * FROM users;"
        results = connectToMySQL("university").query_db(query)
        # print (results) #This will be an array of different dictionaries. name['key']
        users = []
        for user in results:
            users.append(User(user['id'], user['first_name'], user['last_name'], user['email']))
        # print (users) # This will be an array of different objects, which are easier to write and work with "self.field"
        return users #This is being passed to the controller file.

    @classmethod
    def add_user (cls, newuser):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        data = {
            "first_name" : newuser.first_name,
            "last_name" : newuser.last_name,
            "email" : newuser.email
        }
        results = connectToMySQL("university").query_db(query,data) #calling the functions on the mysqlconnection file, needs to include the data
        return results
