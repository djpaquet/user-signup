from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=["POST"])
def username_validate():
    username = request.form['username']
    username_error = ''
    char = ''
    if len(username) >= 3 and len(username) <= 20:
        for character in username:
            if character == ' ':
                username_error = 'Please enter a valid Username that has no spaces'
                username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3-20 characters'
        username = ''
    
    
    return render_template('signup_form.html', username=username, 
                                username_error=username_error)
        
@app.route('/', methods=['POST'])

def email_validate():
    email = request.form['email']
    
app.run()