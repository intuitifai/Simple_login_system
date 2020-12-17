# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:38:25 2020

@author: rahul
"""

from flask import Flask, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__, template_folder='.')
app.secret_key = 'super secret key'

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "1234"
app.config["MYSQL_DB"] = "mydb"

db = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
            if 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("SELECT * FROM login_system WHERE email=%s AND password=%s", (username, password))
                info = cursor.fetchone()
                if info is not None:
                    if info['email'] == username and info['password'] == password:
                        session['loginsuccess'] = True
                        return redirect(url_for('profile'))
                else:
                    return redirect(url_for('index'))

    return render_template("login.html")

@app.route('/new', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "name" in request.form and "username" in request.form and "password" in request.form:
            name = request.form["name"]
            username = request.form["username"]
            password = request.form["password"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO mydb.login_system(name, email, password) VALUES (%s, %s, %s)", (name, username, password))
            db.connection.commit()
            return redirect(url_for('index'))
        
    return render_template("register.html") 

@app.route('/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template('profile.html')

if __name__ == "__main__":
    app.run()