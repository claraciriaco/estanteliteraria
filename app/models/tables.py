from app import db

class User(db.Model):
    _tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String, unique=True)
    autor = db.Column(db.String)
    datainicio = db.Column(db.String)
    datafim = db.Column(db.String)
    obs = db.Column(db.Text)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, title, autor, datainicio, datafim, obs, user_id):
        self.title = title
        self.autor = autor
        self.datainicio = datainicio
        self.datafim = datafim
        self.obs = obs
        self.user_id = user_id

    def __repr(self):
        return "<Book %r>" % self.title
