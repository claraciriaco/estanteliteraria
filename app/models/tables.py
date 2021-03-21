from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String(60))
    password_hash = db.Column(db.String(180))
    
    book = db.relationship('Book', backref='dono', lazy='dynamic')

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
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, index=True)
    autor = db.Column(db.String, index=True)
    datainicio = db.Column(db.String, index=True)
    datafim = db.Column(db.String, index=True)
    obs = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # user = db.relationship('User', db.ForeignKey('users.id'))


    def __init__(self, title, autor, datainicio, datafim, obs):
        self.title = title
        self.autor = autor
        self.datainicio = datainicio
        self.datafim = datafim
        self.obs = obs

    def __repr(self):
        return "<Book %r>" % self.title