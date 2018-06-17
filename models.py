from app import db

from werkzeug.security import generate_password_hash, check_password_hash

listing = db.Table('listing',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    isbn = db.Column(db.String(50))
    author = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    edition = db.Column(db.String(50))

    listing = db.relationship('User', secondary=listing,
                           backref=db.backref('books', lazy='dynamic'))

    def __init__(self, title, isbn, author, condition, edition):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.condition = condition
        self.edition = edition

    def __repr__(self):
        return '<Book %r>' % self.content


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    pw_hash = db.Column('pw_hash', db.String(150))
    email = db.Column(db.String(50))
    is_active = True

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def get_id(self):
        return unicode(self.id)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

