from users_app import app
from flask import render_template,request,redirect,session
from users_app.models.users import User

@app.route('/users', methods=['GET'])
def getAllUsers():
    users = User.get_all_users() #This will grab the array of objects, an object for each line on the table, from the user model.
    return render_template("users.html", users=users) #Sending the information to the HTML.

@app.route('/adduser')
def addUserForm():
    return render_template ("adduser.html")

@app.route('/create', methods=['POST'])
def addUser():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    email = request.form['email']

    newuser = User("",first_name,last_name,email)
    result = User.add_user(newuser)
    print (result)
    return redirect ('/users')