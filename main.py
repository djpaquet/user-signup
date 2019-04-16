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
    #validate username to meet criteria
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
    
    #validate password to meet criteria
    password = request.form['password']
    password_error = ''
    if len(password) >=3 and len(password) <=20:
        for character in password:
            if character == ' ':
                password_error = 'Please enter a valid Password that has no spaces'
                password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password must be at least 6 characters'
        password = ''
    
    #double check verify password that it matches passwordS
    verify_password = request.form['verify_password']
    verify_password_error = ''
    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        password = ''
    
    #validate email to meet citeria
    email = request.form['email']
    email_error = ''

    #use regular expression to validate email
    valid_email = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.])' )
    
    if email =='':
        email=''

    elif not valid_email.match(email):
        email_error = 'Please enter a valid email'
        email = ''
    
    if not username_error and not email_error:
            if not password_error and not verify_password_error:
                return redirect('/hello?username={0}'.format(username))

    return render_template('signup_form.html',username=username, 
                                username_error=username_error,
                                password=password, 
                                password_error=password_error,
                                verify_password=verify_password,
                                verify_password_error=verify_password_error,
                                email=email, email_error=email_error
                                )
        

@app.route('/hello')
def hello():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)
    


app.run()