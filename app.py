from flask import Flask, render_template,flash, redirect, request, session, logging, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm,LoginForm
from models import *

# file upload
UPLOAD_FOLDER = 'C:/Users/91888/Downloads/arxt/arxt/flaskProject2/pdffiles'

# app = Flask(__name__)
app.secret_key = "secret key"

# folder assigne to the settings
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# main page
@app.route('/')
def home():
    return render_template('index.html')


# User registration function

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    # Creating RegistrationForm class object
    form = RegisterForm(request.form)

    # Cheking that method is post and form is valid or not.
    if request.method == 'POST' and form.validate():

        # create new user model here
        new_user = User(

            name = form.name.data,

            username = form.username.data,

            email = form.email.data,

            password = form.password.data )

        # saving user object into data base
        db.session.add(new_user)

        db.session.commit()

        flash('You have successfully registered', 'success')

        # if registration successful, then redirecting to login
        return redirect(url_for('login'))

    else:

        # if method is Get & registarion failed rendering to this page
        return render_template('register.html', form = form)


# Login function
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # verifying that method is post and form is valid
    if request.method == 'POST' and form.validate:
        # checking that user is exist or not by email
        user = User.query.filter_by(email = form.email.data,password=form.password.data).first()

        if user:
                flash('You have successfully logged in.', "success")

                session['logged_in'] = True

                session['email'] = user.email

                session['username'] = user.username
                # After successful login, redirecting to home page
                return redirect(url_for('home'))
        else:

                # if password is in correct , redirect to login page
            flash('Username or Password Incorrect', "Danger")

            return redirect(url_for('login'))
    # rendering login page
    return render_template('login.html', form = form)

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         session['username']=request.form['username']
#         return redirect(url_for('home'))
#     return render_template('login.html')


@app.route('/logout/')
def logout():
    # Removing data from session by setting logged_flag to False.
    session['logged_in'] = False
    # redirecting to home page
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run()
