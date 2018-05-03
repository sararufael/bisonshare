from app import db

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
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name