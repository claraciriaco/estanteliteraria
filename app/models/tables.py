from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String(60))
    password_hash = db.Column(db.String(180))
    
    book = db.relationship('Book', backref='author', lazy='dynamic')
    avaliacao = db.relationship('Avaliacao', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Propriedades de Login
    @property
    def is_authenticated(self):
        return True  
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
  
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, index=True)
    autor = db.Column(db.String, index=True)
    datainicio = db.Column(db.String, index=True)
    datafim = db.Column(db.String, index=True)

    user = db.Column('User', db.ForeignKey('user.id'))
    avaliacao = db.Column('Avaliacao', db.ForeignKey('avaliacao.id'))

    def __repr__(self):
        return "<Book %r>" % self.title

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estrela = db.Column(db.Integer, index=True)
    nota = db.Column(db.String, index=True)

    book = db.Column('Book', db.ForeignKey('book.id'))
    user = db.Column('User', db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Avaliacao %r>" % self.estrela