from flask import Flask, request, render_template, redirect, url_for, flash

from app import app, db

from flask_login import current_user, login_user, logout_user, login_required

from app.models.tables import Book
from app.models.user import User

from app.models.formslivro import LivroForm
from app.models.formuser import LoginForm
from app.models.formcadastrouser import CadastroForm


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

@login.user_loader
def load_user(username):
    return User.get(username)
    
@app.route("/login", methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    User = User.query.filter_by(username=form.data.username).first()
    if User and User.check_password(form.data.password_hash):
      login_user(uUser)
      return redirect(url_for("estante"))
    else:
      flash('erro')
  return render_template("login.html", title="Sig In", form=form)


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for("login"))

@app.route("/estante")
@login_required
def estante():
    Books = Book.query.all()
    return render_template('estante.html', Books=Books)

@app.route("/estante/novo", methods=['GET', 'POST'])
@login_required
def cadastrolivro():
  form = LivroForm()
  if form.validate_on_submit():
    f = Book(title=form.title.data, autor=form.autor.data,
      datainicio=form.datainicio.data, datafim=form.datafim.data, obs=form.obs.data)
    db.session.add(f)
    db.session.commit()
    return redirect(url_for("estante"))
  return render_template("cadastrolivro.html", form=form)
