from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
#application.config['FLASK_DEBUG'] = 1
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(application)

from routes import app
application.register_blueprint(app)

if __name__ == '__main__':
    application.run(debug=True, use_debugger=False, use_reloader=False)
