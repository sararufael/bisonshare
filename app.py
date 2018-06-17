from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
application = Flask(__name__)
application.secret_key = 'super secret key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(application)


app = application

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'

from models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

from routes import main
app.register_blueprint(main)
db.create_all()

