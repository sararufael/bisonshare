from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(app)

@app.route('/')
def login():
    return render_template("form.html")

@app.route('/thanks')
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route('/processform', methods=['GET','POST'])
def processform():
    title = request.form['title']
    isbn = request.form['isbn']
    author = request.form['author']
    condition = request.form['condition']
    edition = request.form['edition']
    book = Book(title, isbn, author, condition, edition)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    isbn = db.Column(db.String(50))
    author = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    edition = db.Column(db.String(50))

    def __init__(self, title, isbn, author, condition, edition):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.condition = condition
        self.edition = edition


if __name__ == '__main__':
    app.run()
