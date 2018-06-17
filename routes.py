
from flask import Blueprint, render_template, request, redirect, url_for, flash, g

from flask_login import login_user, logout_user

main = Blueprint('main', __name__)

from app import db
from models import User, Book

@main.route('/addbook')
def addbook():
    return render_template("form.html")

@main.route('/books')
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@main.route('/processbookform', methods=['GET','POST'])
def processbookform():
    title = request.form['title']
    isbn = request.form['isbn']
    author = request.form['author']
    condition = request.form['condition']
    edition = request.form['edition']
    book = Book(title, isbn, author, condition, edition)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username).first()
    # if the username or password is invalid
    print(registered_user)
    print(registered_user.check_password(password))
    print(registered_user.id)
    if (registered_user is not None) and (registered_user.check_password(password)):

        login_user(registered_user)
        flash('Logged in successfully', 'success')
        print("sandwich")
        return redirect(url_for('main.index'))
    else:
        flash('Username or Password is invalid', 'error')
        print("salad")
    return redirect(url_for('main.login'))




@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@main.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    username_exists, email_exists = False, False
    try:
        username_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()
    except:
        pass

    if username_exists or email_exists:
        flash("Sorry, an account with this username or email already exists", "error")
    else:
        try:
            user = User(username,
                        password,
                        email)
            db.session.add(user)
            db.session.commit()
            flash('User successfully registered', "success")
            html = render_template('email/basic.html',
                                   username=username)
            print("bananas")
            #send_email("Welcome to the BisonShare!", email, html)
        except Exception as e:
            print("failed to create user: %s" % e)
            flash("Oops, something went wrong in creating your account", "error")

    return redirect(url_for('main.login'))
