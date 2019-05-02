from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    


    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verifypassword']
    email = request.form['email']
    

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    username_contains_space = False
    password_contains_space = False

    email_has_at = False
    email_has_dot = False

    for char in username:
        if char == ' ':
            username_contains_space = True

    for char in password:
        if char == ' ':
            password_contains_space = True

    if not username:
        username_error = 'Please enter a username'
        return render_template('index.html', email=email, username_error=username_error)
    if not password:
        password_error = 'Please enter a password'
        return render_template('index.html', email=email, username=username, password_error=password_error)
    if not verify_password:
        verify_password_error = 'Please verify the password'
        return render_template('index.html', email=email, username=username, verify_password_error=verify_password_error)


    if len(username) < 3 or len(username) > 20:
        username_error = 'Username is invalid number of characters (less than 3 or more than 20)'
        return render_template('index.html', email=email, username=username, username_error=username_error)


    if len(password) < 3 or len(password) > 20:
        password_error = 'Password is invalid number of characters (less than 3 or more than 20)'
        return render_template('index.html', email=email, username=username, password_error=password_error)


    if username_contains_space == True:
        username_error = 'Spaces are not allowed in username'
        return render_template('index.html', email=email, username=username, username_error=username_error)

    if password_contains_space == True:
        password_error = 'Spaces are not allowed in password'
        return render_template('index.html', username=username, email=email, password_error=password_error)

    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        return render_template('index.html', username=username, email=email, verify_password_error=verify_password_error)

    if email:
        for char in email:
            if char == ' ':
                email_error = 'Spaces are not allowed in email'
                return render_template('index.html', email=email, username=username, email_error=email_error)
        if len(email) < 3 or len(email) > 20:
            email_error = 'Email length is invalid (either less than 3 characters or more than 20)'
            return render_template('index.html', email=email, username=username, email_error=email_error)
        for char in email:
            if char == '@':
                email_has_at = True
        for char in email:
            if char == '.':
                email_has_dot = True
        if email_has_at != True:
            email_error = 'Email addresses need the @ symbol'
            return render_template('index.html', email=email, username=username, email_error=email_error)
        if email_has_dot != True:
            email_error = 'Email address need the . symbol'
            return render_template('index.html', email=email, username=username, email_error=email_error)


    return render_template('/welcome.html', username=username)







@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html', username=username)


app.run()