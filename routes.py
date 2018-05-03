from app import db

from models import User, Book

from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

@app.route('/')
def registration():
    return render_template("registration.html")

@app.route('/addbook')
def addbook():
    return render_template("form.html")

@app.route('/books')
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route('/processbookform', methods=['GET','POST'])
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

@app.route('/processregistration', methods=['GET','POST'])
def processregistration():
    name = request.registration['name']
    password = request.registration['password']
    email = request.registration['email']
    user = User(name, password, email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/processlogin', methods=['GET','POST'])
def processlogin():
    return redirect(url_for('index'))