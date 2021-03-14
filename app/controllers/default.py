from flask import request, render_template, redirect, url_for

from app import app, db

from flask_login import current_user, login_user, logout_user

from app.models.tables import Book
from app.models.user import User

from app.models.formslivro import LivroForm
from app.models.formuser import LoginForm
from app.models.formuser import CadastroForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
  form = CadastroForm()
  if form.validate_on_submit():
    c = User(username=form.username.data, email=form.email.data)
    c.set_password(password=form.password_hash.data)
    db.create_all()
    db.session.add(c)
    db.session.commit()
    return redirect(url_for("login"))
  return render_template("cadastro.html", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("estante"))
  form = LoginForm()
  if form.validate_on_submit():
    User = User.query.filter_by(username = form.data.username).first()
    if User is None or user.check_password(form.password_hash.data):
      flask.flash('Username e/ou senha inválidos')
      return redirect(self)
      login_user(user, remember_me=form.remember_me.data)
      return redirect(url_for("estante"))
  return render_template("login.html", title="submit", form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("login"))

@app.route("/estante")
def estante():
    Books = Book.query.all()
    return render_template('estante.html', Books=Books)

@app.route("/estante/novo", methods=['GET', 'POST'])
def cadastrolivro():
  form = LivroForm()
  if form.validate_on_submit():
    f = Book(title=form.title.data, autor=form.autor.data,
      datainicio=form.datainicio.data, datafim=form.datafim.data, obs=form.obs.data)
    db.session.add(f)
    db.session.commit()
    return redirect(url_for("estante"))
  return render_template("cadastrolivro.html", form=form)
