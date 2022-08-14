from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') #decorator
def home(): #define a function, put decorator above it
    return render_template("home.html")

