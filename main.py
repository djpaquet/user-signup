from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=["POST"])
def user_validate():
    username = request.form['username']
    username_error = ''
    if len(username) >= 3 and len(username) <= 20:
        for character in username:
            if character == ' ':
                username_error = 'Please enter a valid Username that has no spaces'
                username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3-20 characters'
        username = ''
    
    password = request.form['password']
    password_error = ''
    if len(password) >=3 and len(password) <=20:
        for character in password:
            if character == ' ':
                password_error = 'Please enter a valid Password that has no spaces'
                password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between at least 6 characters'
        password = ''
    
    verify_password = request.form['verify_password']
    verify_password_error = ''
    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        password = ''
    
    
    return render_template('signup_form.html',username=username, 
                                username_error=username_error,
                                password=password, 
                                password_error=password_error,
                                verify_password=verify_password,
                                verify_password_error=verify_password_error
                                )
        
def email_validate():
    email = request.form['email']
    
app.run()