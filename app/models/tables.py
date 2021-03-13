from app import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, index=True)
    autor = db.Column(db.String, index=True)
    datainicio = db.Column(db.String, index=True)
    datafim = db.Column(db.String, index=True)
    obs = db.Column(db.Text)


    def __init__(self, title, autor, datainicio, datafim, obs):
        self.title = title
        self.autor = autor
        self.datainicio = datainicio
        self.datafim = datafim
        self.obs = obs

    def __repr(self):
        return "<Book %r>" % self.title
