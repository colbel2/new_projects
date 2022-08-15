from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['Get', 'Post'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successful!', category = 'success')
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
    data = request.form
    print(data)
    return render_template("login.html",text="testing",user="Colin", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['Get', 'Post'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.', category = 'error')
        elif password1 != password2:
            flash('Passwords must match', category = 'error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category = 'error')
        else:
            new_user = User(email=email,first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='Success')
            #add user to database
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")

