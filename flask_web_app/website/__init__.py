from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views #from views file import name of blueprint, views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')# all the url stored inside file 
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    # from .models import User, Note #import .models would work as well.

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')